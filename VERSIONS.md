# Marketing Skills Versions

Current versions of all skills. Agents can compare against local versions to check for updates.

| Skill | Version | Last Updated |
|-------|---------|--------------|
| ab-testing | 2.0.7 | 2026-11-09 |
| ad-creative | 2.13.0 | 2026-11-10 |
| ai-seo | 2.12.3 | 2026-11-09 |
| analytics | 2.2.5 | 2026-11-09 |
| aso | 2.0.6 | 2026-11-09 |
| attribution | 1.1.9 | 2026-11-09 |
| brand-product-film | 1.0.0 | 2026-11-18 |
| churn-prevention | 2.0.6 | 2026-11-09 |
| co-marketing | 2.0.6 | 2026-11-09 |
| cold-email | 2.2.4 | 2026-11-09 |
| community-marketing | 2.0.5 | 2026-11-09 |
| competitor-profiling | 2.1.8 | 2026-11-09 |
| competitors | 2.3.3 | 2026-11-09 |
| content-strategy | 2.1.8 | 2026-11-09 |
| conversion-tracking | 1.0.6 | 2026-11-09 |
| copy-editing | 2.2.4 | 2026-11-09 |
| copywriting | 2.3.5 | 2026-11-09 |
| cro | 2.0.6 | 2026-11-09 |
| customer-research | 2.0.8 | 2026-11-09 |
| directory-submissions | 2.1.7 | 2026-11-09 |
| emails | 2.1.7 | 2026-11-09 |
| events | 1.0.3 | 2026-11-09 |
| free-tools | 2.0.6 | 2026-11-09 |
| image | 2.0.6 | 2026-11-09 |
| influencer-marketing | 1.4.3 | 2026-11-09 |
| launch | 2.2.3 | 2026-11-09 |
| lead-magnets | 2.1.4 | 2026-11-09 |
| link-building | 1.0.4 | 2026-11-09 |
| marketing-council | 1.0.3 | 2026-11-09 |
| marketing-ideas | 2.0.5 | 2026-11-09 |
| marketing-loops | 1.8.4 | 2026-11-09 |
| marketing-plan | 1.2.5 | 2026-11-09 |
| marketing-psychology | 2.0.3 | 2026-11-09 |
| offers | 1.0.6 | 2026-11-09 |
| onboarding | 2.0.5 | 2026-11-09 |
| ads | 2.7.4 | 2026-11-09 |
| paywalls | 2.1.4 | 2026-11-09 |
| popups | 2.0.4 | 2026-11-09 |
| pricing | 2.1.7 | 2026-11-09 |
| product-marketing | 2.2.3 | 2026-11-09 |
| programmatic-seo | 2.1.3 | 2026-11-09 |
| prospecting | 1.5.3 | 2026-11-09 |
| public-relations | 1.2.4 | 2026-11-09 |
| referrals | 2.2.4 | 2026-11-09 |
| reverse-engineer-marketing | 1.1.4 | 2026-11-09 |
| revops | 2.2.4 | 2026-11-09 |
| sales-enablement | 2.4.3 | 2026-11-09 |
| schema | 2.0.5 | 2026-11-09 |
| seo-audit | 2.2.5 | 2026-11-09 |
| signup | 2.0.3 | 2026-11-09 |
| site-architecture | 2.1.3 | 2026-11-09 |
| sms | 1.1.3 | 2026-11-09 |
| social | 2.5.2 | 2026-11-09 |
| video | 2.4.3 | 2026-11-09 |

## Recent Changes

### 2.15.0 (2026-11-18)

- **brand-product-film** (1.0.0) adds a reusable workflow for rendered product launch films, with CAD and appearance checks, storyboard and animation guidance, resumable segmented rendering, typography, original procedural sound, frame-sequence encoding and delivery verification.

### 2.14.10 (2026-11-10)

- **ad-creative** (2.12.5 → 2.13.0): ten new static ad templates from a review of long-running ads in public ad libraries: Apology Letter ("We're so sorry"), Important Update, Reassurance List ("Stop thinking something is wrong with you"), Simple Guarantee, With / Without, Venn Diagram, Stages (progression comic), Character Story ("This is Mike"), Signs Checklist, and Exaggerated Visual. Their tiers are marked provisional. A new **visual styles** table (dark mode, retro screen, billboard, notice board, presentation slide, whiteboard, handwritten sign, mirror writing, news card, newspaper, vintage, illustration, meme, retro app frame) restyles any template, with rules for styles that borrow a real look: no copied mastheads, no fake system dialogs or "sensitive content" screens, no tabloid claims. Health templates note Meta's personal-attributes and personal-health rules. The format map clarifies that the F-tier fake-native rating covers ads posing as a real interface, not decorative retro frames.

### 2.14.9 (2026-11-09)

Skills load for judgement calls too, even with many other skills installed.

- **50 skills** (patch bump each): the "or asks" part of each description now covers the usual judgement calls in its area: choosing between two options ("which promise to lead with", "screen recording or AI avatar"), whether something is okay or fair ("is it fair to say a rival lacks offline mode", "is this markup allowed"), and whether it's enough ("are six directory listings enough"). Lower-value list items were cut to pay for it, so the pack stays at 18,662 characters and all 53 skills keep their descriptions with 90 other skills installed. On judgement-style prompts nobody read while writing the change, the right skill was picked for about 90% (92.5% twice, 89.6% for the shipped wording, from 66.5%) with 90 other skills installed and 95.3% (from 85.8%) with the pack alone, with no false triggers. programmatic-seo, revops, and signup are unchanged.
- **Trigger eval**: a fourth held-out set (`heldout4.json`, judgement-style), used unread to judge this change.

### 2.14.8 (2026-11-09)

Skills now load for advice and judgement questions, not just requests to make something.

- **Every skill** (patch bump each): each description now names the questions the skill answers ("or asks whether a result is real, when to stop a test, or which version won") next to what it makes. Descriptions that only said "write", "plan", or "create" lost questions like "should we say they lack SSO?" or "where would you look for buyers?": the model answered from general knowledge instead of loading the skill. Total 18,676 characters (from 19,259), so all 53 skills keep their descriptions even with 90 other skills installed (2 dropped before). On a judgement-style test set nobody read while writing the change, the right skill was picked for 87.7% of prompts (from 73.6%) with the pack alone and 73.6% (from about 60%) with 90 other skills installed. Advice-style prompts with other skills installed went from about 84% to 94%, and the original set reaches 100% alone.
- **Trigger eval**: two more held-out sets (`heldout2.json` advice-style, `heldout3.json` judgement-style), seven `heldout.json` prompts now include the material they mention, and missed rows record the model's reply. The README covers run-to-run noise (about plus or minus 4 points on crowded runs) and when to use `--repeat`.

### 2.14.7 (2026-11-09)

- **social** (2.4.3 → 2.5.0): new `references/ship-post.md` for build-in-public posts that start from the commit log (closes #833, by @thiguillaumat-art). It reads the git log and diff since a ref, asks the developer one question (what was annoying or impossible before, and what's different now), picks the one user-visible change, leads with the user's pain rather than the implementation, and drafts one X post and one subreddit post. Hard rules: no number that isn't in the commits, the diff or the developer's answer; no claims about user behaviour nobody reported; flag a user sentence the code doesn't support; drafts only; say so when the week was only chores. SKILL.md links it next to the No AI Tells section, and the description gains a build-in-public trigger. New evals (ids 11–14).

### 2.14.6 (2026-11-09)

The ads operating check now defines "normal variance" as the trailing 6-8 period range, so a single period-over-period swing no longer triggers a change.

- **ads** (2.7.1 → 2.7.2): the operating check pulls the trailing 6-8 periods, calls HOLD when a metric sits inside that range, and treats three or more periods moving the same way as a real movement. Spend, tracking, and broken-page problems, and target-based stop thresholds such as cost per qualified lead above 1.5× TCPL, skip the range gate.
- **marketing-loops** (1.8.1 → 1.8.2): the loop catalog applies the same trailing-range baseline to its performance loops.

### 2.14.5 (2026-11-09)

- **conversion-tracking** (1.0.3 → 1.0.4): the Formidable Forms detector no longer records a conversion after a failed AJAX submit when the visitor later navigates to another same-origin page. A submit whose default was prevented never navigated natively, so its `pagehide` hand-off is skipped, and the sessionStorage marker's TTL now runs from the submit instead of the page exit. Snippet and GTM recipe kept in sync; contract tests added under `tests/assets/`. Reported in #924.

### 2.14.4 (2026-11-09)

- **conversion-tracking** (1.0.2 → 1.0.3): two detector fixes. `generic-ajax-form…36932 tokens truncated…s-as-objection-handlers, the math of stated value, the 4-bonus pattern that works, common failure modes), `scarcity-urgency.md` (honest formats: capacity / cohort / founding-member / inventory / seasonal / bonus-expiry / price-increase; explicit rejection of fake countdown timers and manufactured FOMO; why fake scarcity is uniquely costly), `offer-formats.md` (default offer format by business type — service, course, coaching, info product, high-ticket B2B, agency retainer, self-serve SaaS, direct-response — with what to watch for each), and `examples.md` (six anonymized before/after worked examples spanning fractional CMO, copywriting course, Notion templates, B2B SaaS annual contract, group coaching mastermind, content agency retainer). Includes a banned-vocabulary list (game-changing, revolutionary, 10x, secret, hidden, "limited time" with no actual limit) and explicit anti-patterns (manipulative scarcity, over-promising guarantees, bonus inflation, course-bro aesthetic).
- Cross-references added in `pricing`, `copywriting`, `launch`, and `sales-enablement` descriptions pointing to `offers` for offer construction.
- Total skills: 45.

### 2.4.2 (2026-06-15)

- **ai-seo** (2.0.1 → 2.1.0): added coverage of Google's Open Knowledge Format (OKF), a v0.1 markdown spec for agent-readable site bundles introduced on the Google Cloud blog on 2026-06-12 and shipped inside Knowledge Catalog. New `references/okf.md` reference covers what OKF is (directory of cross-linked markdown files with YAML frontmatter — `type` required, plus `title`/`description`/`resource`/`tags`/`timestamp` recommended), honest framing (Google built it for data-team catalog metadata; site-readable repurposing popularized by Suganthan Mohanadasan is a clever secondary use), what it does for AI search today (nothing immediate; protocol-layer registration like early schema.org adoption), where OKF fits in the agent-readable stack alongside `sitemap.xml` / `robots.txt` / `llms.txt` / `/pricing.md` / schema, three ways to ship a bundle (Suganthan's free web generator, his pending WordPress plugin, or by hand), hosting guidance (`yoursite.com/okf/index.md` plus an `llms.txt` line pointing to it), when to skip (closed platforms like Wix/Squarespace, very small sites, sites without other machine-readable files), and what to watch (v1.0 spec, AI engine adoption signals). `SKILL.md` adds a brief OKF subsection under "Machine-Readable Files for AI Agents" pointing to the reference. Frontmatter description extended with new triggers: `llms.txt`, `OKF`, `Open Knowledge Format`, `knowledge bundle`, `agent-readable site`. `references/platform-ranking-factors.md` Google AI Overviews section gets an OKF callout framing it as a "register early" protocol bet rather than a confirmed ranking signal.

### 2.4.1 (2026-06-10)

- Renamed `pr` skill to `public-relations` to avoid collision with pull-request skills in other Claude Code plugins (common naming for code-review / GitHub PR automation). The skill description already disambiguated from pull requests, but the directory name `pr` was still ambiguous to skill resolvers and to users typing `/pr`. The rename happened within hours of the initial v2.4.0 publish, before meaningful install adoption. No content changes; skill version stays at 1.0.0. All cross-references in `social/SKILL.md`, `VERSIONS.md`, and `README.md` updated accordingly.

### 2.4.0 (2026-06-10)

- Added `public-relations` skill (originally shipped as `pr`, renamed in v2.4.1) for public relations / earned media work — pitching journalists, newsjacking trending stories, responding to press requests (HARO/Connectively, Qwoted, Featured, Help A B2B Writer), and building the owned-media foundation (press page + media kit). Four PR modes (reactive / proactive / inbound / owned), explicit when-to-skip framing, and a banned-vocabulary list. References include: `newsjacking.md` (detect → score → angle → pitch loop with newsworthiness scoring rubric, 7 angle templates, Google News / HN / Reddit curl recipes, failure modes); `journalist-pitching.md` (media list construction, journalist fit scoring, 6 pitch templates by angle — data story / exclusive launch / op-ed / customer story / trend connector / newsjack response — subject-line craft, embargo etiquette, follow-up cadence); `press-platforms.md` (daily triage workflow, response template, ROI reality check); `media-outlets.md` (tiered list of tech press, SaaS, AI, devtools, business outlets, newsletters, podcasts, vertical press, regional press — explicitly scoped to journalist-driven outlets, with startup directories deferred to `directory-submissions`). Scope is enforced via cross-references: the `public-relations` skill handles earned media; `directory-submissions` handles Product Hunt / BetaList / SaaS directories; `launch` handles the broader launch moment.
- **social** (2.0.0 → 2.1.0): added `references/listening.md` for engagement triage — a daily loop for surfacing the top posts to comment on rather than scrolling feeds. Includes a 5-dimension scoring rubric (ICP fit, intent signal, reach potential, comment opportunity, recency), comment quality tiers, curl-based recipes for Reddit / HN Algolia / Bluesky (no auth required), and a browser-driven workflow for LinkedIn and X via `dev-browser` with persistent session. Added `references/listening-sources-template.md` — a copyable starter for `.agents/listening-sources.md` covering brand/category context, ICP definition, target accounts per platform, intent keywords, subreddits, saved-search URLs, and a do-not-engage list. SKILL.md Engagement Strategy section now links to the listening reference.
- Total skills: 44.

### 2.3.0 (2026-05-27)

- Added `marketing-plan` skill — comprehensive AARRR-structured marketing plan generator. Produces a 13-section Notion-paste-ready plan document (executive summary, strategic frame, current state, AARRR breakdown, 90-day roadmap, 12-month outlook with funding-stage capability unlocks, marketing operations stack mapping skills + MCPs to AARRR stages, tactical idea bank cross-referencing all 139 `marketing-ideas` to AARRR + client-specific status, measurement framework, RACI, open decisions). Customized for current budget, team, stage, and tooling stack. Three-phase workflow: INIT (research + intake), REVIEW (section-by-section walkthrough), FINALIZE (compile + verify + optional publish to shared repo). References include methodology, plan-template, aarrr-framework, current-state-rubric (self-contained 17-section scoring rubric), ops-stack-mapping, idea-cross-reference (139-idea AARRR mapping), funding-stage-unlocks, measurement-framework, client-types (variations by B2B SaaS / D2C / hardware-hybrid / marketplace / dev tool / clinical / commerce), example-quietude (anonymized canonical reference plan, based on a real fCMO engagement with names/identifying details changed), budget-planning (two scientific methods for setting the marketing budget — Revenue-Based 5–40% of ARR, and Goal-Based formula reverse-engineered from the revenue target; plus blended CAC calculation, the 10–20% experimental buffer rule, the 3-3-2-2-2 VC growth path, and the forecasting reality check), growth-patterns (the real shape of SaaS growth — $0–10K / $10K–100K / $100K–1M phases with binding constraints, linear vs step-function vs S-curve patterns, and Channel × Product × Market layering), and team-and-agency-model (the strategy-in-house / execution-outsourced principle, three core functions Growth/Product/Content, π-shaped marketer framework, title progression Manager → Lead → Director → VP → Chief, agency selection framework, and the three-stage scaling model Early/Growth/Scale). Budget, growth-pattern, and team frameworks drawn from *Founding Marketing* by Corey Haines.
- Total skills: 43.

### 2.2.0 (2026-05-26)

- Added `prospecting` skill for building qualified prospect lists across SaaS, B2B, and local SMB motions. Includes shared 5-phase framework (ICP → discovery → qualify → score → output) plus branch-specific references (saas-prospecting, b2b-prospecting, local-prospecting), data-sources guide covering Apollo / Clay / ZoomInfo / Clearbit / Hunter / Snov / Truelist / RB2B / Sales Nav / BuiltWith / Crunchbase / GitHub, and compliance reference (CAN-SPAM, GDPR, CASL, platform ToS).
- Added `tools/clis/github-prospects.js` CLI for pulling GitHub stargazers, forkers, and watchers as a developer-intent signal — with pagination, enrichment, filter-based early termination, and CSV output.
- Added new tool integration docs: `truelist` (email deliverability validation, OpenAPI-aligned), `github` (REST API for prospecting), `firecrawl` (single-target page scraping), `browserbase` (real Chromium for JS-heavy pages or interaction).
- **ads** (2.0.0 → 2.0.1): added Google RSA Output Spec section enforcing 15 headlines × 30 chars, 4 descriptions × 90 chars, ad group structure labels, ≥8 negative keywords, ≥4 sitelinks/callouts, output ordering to avoid truncation, and a self-check before responding. Includes optional Brazilian medical (CFM) compliance rules when product context indicates that vertical.
- Added `sequenzy` tool integration (email marketing platform with MCP support).
- Fixed plugin.json version drift (was stuck at 1.9.0 across three releases) — `sync-skills.js` now auto-syncs `plugin.json` version to `marketplace.json` on every change. Closes #323.
- Added skill install artifacts (`.agents/`, `.claude/`, `skills-lock.json`) to `.gitignore`.
- Total skills: 42.

### 2.1.0 (2026-05-21)
- Added `sms` skill for SMS/MMS marketing — welcome flows, abandoned cart, post-purchase, win-back, promotional sends, and transactional/auth. Includes compliance reference (TCPA, A2P 10DLC, GDPR, CASL), sequence templates with character counts, and platform comparison (Klaviyo, Postscript, Attentive, Twilio, Brevo, SimpleTexting, Customer.io).
- Total skills: 41

### 2.0.1 (2026-05-18)

Content patch — no breaking changes, no new skills.

- **ai-seo** (2.0.0 → 2.0.1): aligned with Google's official AI features optimization guide. Added sections for Google's stance on AI optimization, query fan-out, agentic experiences (including UCP), explicit "what NOT to do" (scaled content abuse, etc.), and Search Console expectations. Reframed llms.txt / pricing.md / schema markup recommendations as "Google says not required, helpful for non-Google AI engines." Moved content-type tactics to `references/content-types.md` (added local/ecom Merchant Center + Business Profile guidance per Google).
- **image** (2.0.0 → 2.0.1): refreshed model lineup to current May 2026 releases — Nano Banana / Nano Banana Pro family naming, Flux Pro 1.1 + Kontext + Dev + Schnell variants, Ideogram 3.0, ChatGPT Images 2.0 / GPT Image, Midjourney v7, Recraft V3, SD 3.5 / SDXL. Updated decision tree and trigger phrases.
- **video** (2.0.0 → 2.0.1): refreshed model lineup — Sora 2 promoted from limited-availability caveat, Kling 2.5/3.0, added Seedance (ByteDance), Hailuo / MiniMax (character consistency), Hunyuan Video / Wan 2 (open-weight self-hosted), Pika 2.x. New "Quick picks" guide.

Total skills: 40 (unchanged).

### 2.0.0 (2026-05-05)

**Breaking changes** — Users must reinstall skills after this update.

#### Skill Renames (17)
| Old Name | New Name |
|----------|----------|
| ab-test-setup | ab-testing |
| analytics-tracking | analytics |
| aso-audit | aso |
| competitor-alternatives | competitors |
| email-sequence | emails |
| free-tool-strategy | free-tools |
| launch-strategy | launch |
| onboarding-cro | onboarding |
| paid-ads | ads |
| paywall-upgrade-cro | paywalls |
| popup-cro | popups |
| pricing-strategy | pricing |
| product-marketing-context | product-marketing |
| referral-program | referrals |
| schema-markup | schema |
| signup-flow-cro | signup |
| social-content | social |

#### Consolidations (1)
- `page-cro` + `form-cro` → `cro` (form content moved to `references/form.md`)

#### Why 2.0?
- Shorter, cleaner skill names
- Consistent naming conventions (no more `-strategy`, `-setup`, `-cro` suffixes)
- Consolidated CRO into single skill with references
- All cross-references updated across 100+ files

**Total skills: 40**

### 1.10.0 (2026-05-04)
- Added `co-marketing` skill for partner identification, joint campaigns, and co-marketing strategy
- Total skills: 41

### 2026-04-24
- Added `image` skill for AI image generation, design tools, profile/listing banners, and optimization
- Added `video` skill for AI video production (Hyperframes, HeyGen, Veo, Runway, Kling)
- Added short-form video section to `social` (1.3.0) — TikTok, Reels, Shorts frameworks
- Added HeyGen and Hyperframes tool integration guides
- Fixed plugin marketplace: `source` field now passes Claude Code schema validation (#270)
- Added proper `plugin.json` manifest with `"skills": "./skills"`
- Total skills: 40

### 2026-04-21
- Added `directory-submissions` skill for Product Hunt, G2, AI directories, and backlink strategy
- Added `competitor-profiling` skill for competitive intelligence research
- Added international SEO & localization section to `seo-audit` (1.2.0)
- Added conversion tracking reference to `ads` (cross-platform pixel setup)
- Added Zapier SDK integration for 8,000+ app access
- Fixed plugin loading: removed `./` prefix from marketplace.json skill paths (#243)
- Hardened CLI tools: Supermetrics API key moved to header, ZoomInfo JWT masked by default
- Fixed community-marketing YAML frontmatter (#240)
- Fixed Zapier webhook URL validation (#247)
- Added missing skills to VERSIONS.md (aso, community-marketing, customer-research — shipped in prior releases)
- Total skills: 38

### 2026-03-14
- Added `lead-magnets` skill for lead magnet strategy, format selection, and conversion optimization
- Added Composio integration layer for MCP access to OAuth-heavy tools (HubSpot, Salesforce, Meta Ads, LinkedIn Ads, Google Sheets, Slack, Notion, etc.)
- Added headless CMS integration guides (Sanity, Contentful, Strapi) with headless-cms reference
- Added 197 evals across all 33 skills for automated quality testing
- Optimized all 32 skill descriptions for better trigger phrase matching
- Replaced rigid imperatives with reasoning-based guidance across all skills
- Added 10 new CLI tools (airops, clay, close, coupler, crossbeam, outreach, pendo, similarweb, supermetrics, zoominfo)
- Added 13 new integration guides
- Bumped all 32 existing skills from 1.1.0 → 1.2.0

### 2026-02-27
- Migrated context path from `.claude/` to `.agents/` for agent-agnostic compatibility
- All skills now check `.agents/product-marketing.md` first, with `.claude/` fallback for older setups
- Updated install paths in README to reference `.agents/skills/`
- Bumped all 32 skills from 1.0.0 → 1.1.0

### 2026-02-22
- Added `revops` skill for revenue operations, lead lifecycle, scoring, routing, pipeline management, and CRM automation
- Added `sales-enablement` skill for sales decks, one-pagers, objection handling, demo scripts, and sales playbooks

### 2026-02-21
- Added `site-architecture` skill for website structure planning, page hierarchy, navigation design, URL structure, and internal linking strategy

### 2026-02-18
- Added `ai-seo` skill for AI search optimization (AEO, GEO, LLMO, AI Overviews)
- Moved AEO/GEO content patterns from `seo-audit` references to `ai-seo` skill
- Added `churn-prevention` skill for cancel flows, save offers, dunning, and payment recovery

### 2026-02-17
- Added `ad-creative` skill for bulk ad creative generation and performance-based iteration
- Added 51 zero-dependency CLI tools for marketing platforms (`tools/clis/`)
- Added 31 new integration guides (`tools/integrations/`)
- Added 4 email outreach CLIs: hunter, snov, lemlist, instantly
- Security hardening: header auth for meta-ads, URL encoding, input validation
- All CLIs reviewed via independent codex audit (auth, security, error handling, consistency)

### 2026-01-27
- Initial version tracking added
- Added tools registry with 29 integration guides
