"""Validate rendered PNG sequences, apply editable titles and assemble standalone clips and a master."""
import argparse
import json
import math
import re
import shutil
import struct
import subprocess
from pathlib import Path


def png_size(path):
    with path.open("rb") as image:
        header = image.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Invalid PNG header: {path}")
    return struct.unpack(">II", header[16:24])


def run(ffmpeg, root, arguments, capture=False):
    result = subprocess.run([str(ffmpeg), "-hide_banner", "-nostdin", *map(str, arguments)],
                            cwd=root, check=True, capture_output=capture,
                            text=capture, encoding="utf-8" if capture else None,
                            errors="replace" if capture else None)
    return result


def encode(manifest_path, ffmpeg, output, dry_run=False):
    root = manifest_path.resolve().parent
    config = json.loads(manifest_path.read_text(encoding="utf-8"))
    fps = int(config["fps"])
    width, height = int(config["width"]), int(config["height"])
    if fps <= 0 or width <= 0 or height <= 0 or width % 2 or height % 2:
        raise ValueError("Frame rate and even output dimensions must be positive.")
    audio = (root/config["audio"]).resolve()
    font = (root/config["font"]).resolve()
    if not audio.is_file() or not font.is_file():
        raise FileNotFoundError("The audio and title font must exist.")
    shots = config["shots"]
    if not shots:
        raise ValueError("The manifest must contain shots.")
    names = [shot["name"] for shot in shots]
    if len(set(names)) != len(names):
        raise ValueError("Shot names must be unique.")
    for shot in shots:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", shot["name"]):
            raise ValueError("Shot names must be simple filename stems.")
        frames = int(shot["frames"])
        seconds = float(shot["seconds"])
        if frames <= 0 or not math.isfinite(seconds) or abs(frames/fps-seconds) > 1e-6:
            raise ValueError(f"Inconsistent timing for {shot['name']}")
        directory = root/shot["directory"]
        missing = [i for i in range(1, frames+1)
                   if not (directory/f"{i:04d}.png").is_file()]
        if missing:
            raise ValueError(f"{shot['name']} has missing frames: {missing[:12]}")
        for index in (1, frames):
            if png_size(directory/f"{index:04d}.png") != (width, height):
                raise ValueError(f"Incorrect image dimensions for {shot['name']}")
    duration = sum(int(shot["frames"]) for shot in shots)/fps
    if dry_run:
        print(json.dumps({"shots": len(shots), "duration": duration,
                          "frames": round(duration*fps), "size": [width,height]}))
        return

    output = output.resolve()
    clips_folder = output/"Clips"
    text_folder = output/"Text"
    asset_folder = output/"EncodingAssets"
    clips_folder.mkdir(parents=True, exist_ok=True)
    text_folder.mkdir(parents=True, exist_ok=True)
    asset_folder.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(font, asset_folder/"title.ttf")
    font_filter = "EncodingAssets/title.ttf"
    elapsed = 0
    clip_paths = []
    for shot in shots:
        name, seconds, frames = shot["name"], float(shot["seconds"]), int(shot["frames"])
        filters = ["setsar=1"]
        for index, title in enumerate(shot.get("titles", [])):
            text_file = text_folder/f"{name}_{index}.txt"
            text_file.write_text(title["text"], encoding="utf-8")
            text_filter = text_file.relative_to(output).as_posix()
            current_font = font_filter
            if title.get("font"):
                alternate = (root/title["font"]).resolve()
                font_name = f"{name}_{index}.ttf"
                shutil.copyfile(alternate,asset_folder/font_name)
                current_font = "EncodingAssets/"+font_name
            fade = f"min(1,max(0,(t-.2)/.5))*min(1,max(0,({seconds}-.1-t)/.3))"
            filters.append(
                f"drawtext=fontfile={current_font}:textfile={text_filter}:expansion=none:"
                f"x={int(title.get('x',140))}:y={int(title.get('y',840))}:"
                f"fontsize={int(title.get('size',32))}:fontcolor=0x{title.get('color','F0E5D1')}:"
                f"alpha='{fade}':shadowcolor=black@0.25:shadowx=0:shadowy=2")
        graph = "[0:v]"+",".join(filters)+"[base]"
        arguments = ["-v","error","-y","-framerate",fps,"-start_number",1,
                     "-i",root/shot["directory"]/"%04d.png",
                     "-ss",f"{elapsed:.8f}","-i",audio]
        if shot.get("show_logo"):
            logo = (root/config["logo"]).resolve()
            arguments += ["-loop","1","-i",logo]
            graph += ";[2:v]scale=225:-1,format=rgba[logo];[base][logo]overlay=140:310:shortest=1[composite]"
        else:
            graph += ";[base]null[composite]"
        finishing = []
        if shot.get("fade_in"):
            finishing.append("fade=t=in:st=0:d=0.35")
        if shot.get("fade_out"):
            finishing.append(f"fade=t=out:st={max(0,seconds-.35)}:d=0.35")
        graph += ";[composite]"+(",".join(finishing) if finishing else "null")+"[v]"
        clip = clips_folder/f"{name}.mp4"
        partial = clips_folder/f"{name}.partial.mp4"
        run(ffmpeg, output, arguments+[
            "-filter_complex",graph,"-map","[v]","-map","1:a:0",
            "-frames:v",frames,"-t",seconds,"-r",fps,
            "-c:v","libx264","-crf","17","-preset","medium","-threads","4",
            "-pix_fmt","yuv420p","-color_primaries","bt709","-color_trc","bt709",
            "-colorspace","bt709","-c:a","aac","-b:a","192k",
            "-af",f"afade=t=in:st=0:d=0.08,afade=t=out:st={max(0,seconds-.1)}:d=0.1",
            "-movflags","+faststart",partial])
        partial.replace(clip)
        clip_paths.append(clip)
        elapsed += seconds
        print("ENCODED",name,flush=True)

    listing = output/"clips.ffconcat"
    listing.write_text("ffconcat version 1.0\n"+
                       "".join(f"file 'Clips/{clip.name}'\n" for clip in clip_paths),
                       encoding="utf-8")
    master_name = config.get("master_name","Launch.mp4")
    if Path(master_name).name != master_name or not master_name.lower().endswith(".mp4"):
        raise ValueError("master_name must be a plain MP4 filename.")
    master = output/master_name
    partial = master.with_name(master.stem+".partial.mp4")
    run(ffmpeg, output, [
        "-v","error","-y","-f","concat","-safe","0","-i",listing,"-i",audio,
        "-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","aac","-b:a","192k",
        "-t",duration,"-movflags","+faststart",partial])
    partial.replace(master)
    decoded = run(ffmpeg, output, [
        "-v","info","-i",master,"-map","0:v:0","-map","0:a:0","-f","null","-"],capture=True)
    log = decoded.stderr
    if f"{width}x{height}" not in log or not re.search(rf"frame=\s*{round(duration*fps)}\s", log):
        raise RuntimeError("Decoded master does not match expected dimensions or frame count.")
    (output/"verification.log").write_text(log,encoding="utf-8")
    print(json.dumps({"master":str(master),"duration":duration,
                      "frames":round(duration*fps),"clips":len(clip_paths)}),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest",type=Path)
    parser.add_argument("--ffmpeg",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--dry-run",action="store_true")
    args = parser.parse_args()
    encode(args.manifest,args.ffmpeg.resolve(),args.output,args.dry_run)


if __name__ == "__main__":
    main()

