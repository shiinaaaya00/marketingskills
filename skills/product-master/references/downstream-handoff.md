# Downstream Handoff

`downstream_handoff.json` is the compact machine-readable input for downstream skills.

## Required content

- identity
- variants
- SKUs
- pricing
- dimensions
- physical identity
- verified features
- included items
- approved claims
- prohibited claims
- approved assets
- PRD decisions
- open issues
- master version
- source audit status

## Consumer behavior

### product-video
Use product identity lock, approved visual assets, verified features, video-approved claims, prohibited claims, and PRD video requirements.

### PDP
Use positioning, PDP-approved claims, variants/SKUs, price, included items, dimensions, and approved assets.

### product-images
Use geometry/material/color lock, approved references, included items, and prohibited visual inventions.

### SEO/GEO
Use official name, category, verified features, approved claims, use cases, and market scope.

### EDM / Ads / Affiliate / Influencer
Use only claims allowed for that channel.

## Freshness

Store master version and generation timestamp.

A downstream artifact is stale if it relies on a fact that later becomes `SUPERSEDED`, `CONFLICT`, or `PROHIBITED`.
