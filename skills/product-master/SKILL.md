---
name: product-master
description: Build and maintain a reusable single source of truth for an ecommerce or physical product from raw specs, spreadsheets, images, packaging, BOM/cost, SKU/inventory, listings, approved copy, compliance files, and notes. Use to produce PRODUCT_MASTER, PRODUCT_PRD, CLAIMS_MATRIX, ASSET_INDEX, SOURCE_AUDIT, LAUNCH_READINESS, CHANGELOG, and a machine-readable downstream handoff for product-video, PDP, images, SEO, EDM, ads, affiliate, marketplace, and launch workflows. Detect conflicts, preserve provenance, classify unverified/prohibited claims, and never silently invent or reconcile product facts.
---

# Product Master

Create and maintain the product's authoritative operational source of truth.

This skill has two separate layers:

1. **Fact layer** — establish what the product actually is.
2. **Execution layer** — translate verified product truth into a reusable Product PRD and downstream handoff.

Never collapse these layers into one document.

## Core outputs

Create and maintain:

- `work/PRODUCT_MASTER.md`
- `work/product_master.json`
- `work/PRODUCT_PRD.md`
- `work/CLAIMS_MATRIX.md`
- `work/ASSET_INDEX.md`
- `work/SOURCE_INVENTORY.md`
- `work/SOURCE_AUDIT.md`
- `work/LAUNCH_READINESS.md`
- `work/CHANGELOG.md`
- `work/downstream_handoff.json`

## Non-negotiable rules

1. Never invent product facts.
2. Never use competitor/reference material as evidence for this product.
3. Never silently reconcile conflicting sources.
4. Preserve source provenance for every material fact.
5. Distinguish `LOCKED`, `VISUAL_ONLY`, `DERIVED`, `UNVERIFIED`, `CONFLICT`, `PROHIBITED`, and `SUPERSEDED`.
6. Images can support visible geometry, finish, controls, labels, packaging, and clearly visible included items; images do not automatically verify technical performance.
7. Derived values must record formula and inputs.
8. Public marketing claims require claim status and channel permission.
9. Keep historical values in `CHANGELOG.md`; do not erase superseded facts.
10. Downstream skills should consume the current master/handoff before raw notes.

## Initialize a product project

Run:

`python scripts/init_product.py <project-dir>`

Put sources under:

- `inputs/brand/`
- `inputs/specs/`
- `inputs/product-images/`
- `inputs/packaging/`
- `inputs/bom-cost/`
- `inputs/sku-inventory/`
- `inputs/listings/`
- `inputs/copy-marketing/`
- `inputs/compliance/`
- `inputs/research/`
- `inputs/notes/`

Do not store project-specific source files inside the reusable skill directory.

## Workflow

### 1. Inventory sources

Read:
- `references/source-priority.md`
- `references/extraction-rules.md`

Run:

`python scripts/inventory_sources.py <project-dir>`

Assign stable IDs such as `SRC-001`.

Update:
- `SOURCE_INVENTORY.md`
- `SOURCE_AUDIT.md`

### 2. Extract facts

Read `references/data-model.md`.

Populate:
- `product_master.json`
- `PRODUCT_MASTER.md`

Each fact must include:
- `fact_id`
- `category`
- `name`
- `value`
- `unit` when applicable
- `scope`
- `status`
- `source_refs`
- `effective_date` when known
- `derivation` when derived
- `notes`

Do not mark a fact `LOCKED` without acceptable evidence and without checking higher-priority conflicts.

### 3. Resolve conflicts

Read `references/conflict-resolution.md`.

Resolution order:
1. verify same field and scope;
2. compare source authority;
3. compare date/revision;
4. compare approved/final vs draft;
5. check variant/market/package scope;
6. check measured vs derived;
7. keep `CONFLICT` if unresolved.

Never use majority voting.

### 4. Build claims matrix

Read `references/claims-rules.md`.

Create `CLAIMS_MATRIX.md`.

Claim statuses:
- `APPROVED`
- `APPROVED_WITH_QUALIFIER`
- `INTERNAL_ONLY`
- `UNVERIFIED`
- `PROHIBITED`
- `SUPERSEDED`

Every public claim must reference supporting fact IDs and permitted channels.

### 5. Build asset index

Read `references/asset-rules.md`.

Create `ASSET_INDEX.md`.

Asset statuses:
- `APPROVED`
- `REFERENCE_ONLY`
- `NEEDS_RETOUCH`
- `NEEDS_REVIEW`
- `OBSOLETE`
- `PROHIBITED`

AI-generated concepts are not automatically product truth.

### 6. Generate Product PRD

Read `references/prd-generation.md`.

Generate `PRODUCT_PRD.md` only after the fact layer is audited enough to support it.

Strategic decisions must be labeled:
- `DECIDED`
- `PROPOSED`
- `OPEN`

Do not write proposed strategy back into PRODUCT_MASTER as verified fact.

### 7. Assess readiness

Read `references/qa.md`.

Create `LAUNCH_READINESS.md`.

Statuses:
- `READY`
- `READY_WITH_LIMITATIONS`
- `BLOCKED`
- `NOT_REQUIRED`
- `UNVERIFIED`

### 8. Build downstream handoff

Read `references/downstream-handoff.md`.

Run:

`python scripts/build_handoff.py <project-dir>`

Preferred downstream consumption order:
1. `downstream_handoff.json`
2. `PRODUCT_MASTER.md`
3. `PRODUCT_PRD.md`
4. `CLAIMS_MATRIX.md`
5. `ASSET_INDEX.md`

Typical consumers:
- `product-video`
- product images/media
- PDP/CRO
- Shopify listing
- SEO/GEO
- EDM
- ads
- affiliate/AWIN
- influencer
- marketplace
- product-launch workflows

### 9. Update/version

Read `references/versioning.md`.

When new information arrives:
1. inventory the new source;
2. compare with current locked facts;
3. identify additions, changes, and conflicts;
4. update only with evidence;
5. mark old facts `SUPERSEDED` where applicable;
6. append `CHANGELOG.md`;
7. rebuild handoff;
8. rerun validation;
9. flag stale downstream artifacts.

Compare two masters with:

`python scripts/compare_versions.py <old.json> <new.json>`

### 10. Validate

Run:

`python scripts/validate_product.py <project-dir>`

Validation must check:
- required files;
- product identity;
- source-backed locked facts;
- derivation metadata;
- unresolved conflicts;
- downstream readiness consistency.

## Final project statuses

Use one:
- `INGESTED`
- `AUDITED`
- `MASTER_COMPLETE`
- `PRD_COMPLETE`
- `READY_FOR_DOWNSTREAM`
- `BLOCKED`

Never claim `READY_FOR_DOWNSTREAM` while material identity/spec conflicts remain unresolved.

## Communication

- Use the user's preferred language for internal collaboration.
- Use target-market language for public-facing copy.
- Preserve exact names, model numbers, SKUs, units, qualifiers, and approved claim wording.
- When information is missing, state exactly what is missing and what it blocks.
