"""Generate an original synthetic stereo score from a duration and impact-cue settings file."""
import argparse
import json
import math
import wave
from pathlib import Path

import numpy as np


def generate(settings, output):
    duration = float(settings["duration"])
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("Duration must be finite and positive.")
    impacts = [float(value) for value in settings.get("impacts", [])]
    if any(not math.isfinite(value) or value < 0 or value >= duration for value in impacts):
        raise ValueError("Impact times must fall within the duration.")
    rate = 48000
    times = np.arange(round(rate * duration), dtype=np.float64) / rate
    stereo = np.zeros((len(times), 2), dtype=np.float64)
    random = np.random.default_rng(int(settings.get("seed", 17)))
    tau = 2 * math.pi

    def mix(signal, pan=0):
        stereo[:, 0] += signal * math.sqrt((1-pan)/2)
        stereo[:, 1] += signal * math.sqrt((1+pan)/2)

    chords = [
        (65.406, 130.813, 155.563, 195.998),
        (51.913, 103.826, 155.563, 261.626),
        (58.270, 116.541, 174.614, 233.082),
        (65.406, 130.813, 164.814, 261.626),
    ]
    for index, notes in enumerate(chords):
        start = max(0, duration * index / 4 - .8)
        end = min(duration, duration * (index+1) / 4 + 1.3)
        envelope = np.minimum(np.clip((times-start)/1.2, 0, 1),
                              np.clip((end-times)/1.6, 0, 1))
        envelope = np.sin(envelope * math.pi/2)**2
        for note_index, frequency in enumerate(notes):
            phase = random.uniform(0, tau)
            for detune, pan in ((-.12, -.6), (.15, .6)):
                sound = np.sin(tau*(frequency+detune)*times+phase)
                sound += .12*np.sin(tau*frequency*2*times+phase)
                mix(sound * envelope * (.038 if note_index < 2 else .023), pan)

    for cue in impacts:
        elapsed = np.maximum(0, times-cue)
        envelope = (times >= cue) * (1-np.exp(-elapsed*100))
        bass = np.sin(tau*(43*elapsed + .9*(1-np.exp(-elapsed*16))))
        mix(.40*bass*envelope*np.exp(-elapsed*4))
        noise = random.normal(0, 1, len(times))
        air = np.convolve(noise, np.ones(13)/13, "same")
        air -= np.convolve(air, np.ones(64)/64, "same")
        swell = np.clip((times-cue+.45)/.45, 0, 1)**2 * np.exp(-elapsed*6)
        mix(.18*air*swell, -.4)
        mix(.15*air*swell, .5)

    for cue in np.arange(duration*.30, duration-.8, .5):
        elapsed = np.maximum(0, times-cue)
        frequency = (261.626, 311.127, 391.995, 523.251)[int(cue*2) % 4]
        envelope = (times >= cue)*(1-np.exp(-elapsed*130))*np.exp(-elapsed*8)
        mix(.025*np.sin(tau*frequency*elapsed)*envelope,
            .35*math.sin(cue))

    stereo *= np.clip(times/.25, 0, 1)[:, None]
    stereo *= np.clip((duration-times)/1.25, 0, 1)[:, None]
    stereo = np.tanh(stereo*1.6)
    peak = np.max(np.abs(stereo))
    if peak > 0:
        stereo *= .76/peak
    output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output), "wb") as audio:
        audio.setparams((2, 2, rate, 0, "NONE", "not compressed"))
        audio.writeframes((stereo*32767).astype("<i2").tobytes())
    print(json.dumps({"output": str(output), "duration": duration, "peak": .76}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("settings", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    generate(json.loads(args.settings.read_text(encoding="utf-8")), args.output)


if __name__ == "__main__":
    main()

