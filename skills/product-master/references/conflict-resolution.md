# Conflict Resolution

## Types

Numeric, unit, naming, SKU, variant, market, packaging, included-item, claim, version.

## Sequence

1. Confirm same field and scope.
2. Compare authority.
3. Compare revision/date.
4. Compare approved/final vs draft.
5. Check explicit supersession.
6. Check measured vs derived.
7. Check market/variant/package scope.
8. Keep `CONFLICT` if unresolved.

## Safe behavior

Exclude unresolved conflicts affecting identity, SKU, dimensions, price, included items, core features, safety/compliance, or public claims from public downstream use.

Never use majority voting.
