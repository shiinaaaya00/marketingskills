# Product Data Model

## Recommended categories

`IDENTITY`, `VARIANT`, `SKU`, `PRICE`, `DIMENSION`, `WEIGHT`, `MATERIAL`, `FINISH`, `COLOR`, `CONTROL`, `POWER`, `BATTERY`, `LIGHT`, `OUTPUT`, `PERFORMANCE`, `TIMER`, `NOISE`, `CAPACITY`, `COMPATIBILITY`, `INCLUDED_ITEM`, `PACKAGING`, `CERTIFICATION`, `WARRANTY`, `LOGISTICS`, `COST`, `INVENTORY`, `SCENT`, `INGREDIENT`, `CARE`, `SAFETY`, `MARKET`, `OTHER`.

## Fact IDs

Examples:

- `IDENTITY.PRODUCT_NAME`
- `IDENTITY.MODEL`
- `VARIANT.COLOR.CREAM`
- `SKU.CREAM.US`
- `DIMENSION.HEIGHT`
- `LIGHT.COLOR_TEMPERATURE`
- `NOISE.MAX_DB`
- `INCLUDED_ITEM.OIL_BOTTLE.QTY`
- `PRICE.US.RETAIL`

## Fact object

```json
{
  "fact_id": "DIMENSION.HEIGHT",
  "category": "DIMENSION",
  "name": "Overall height",
  "value": 30,
  "unit": "cm",
  "scope": {"market":"ALL","variant":"ALL"},
  "status": "LOCKED",
  "source_refs": ["SRC-003"],
  "effective_date": "2026-11-12",
  "derivation": null,
  "notes": ""
}
```

## Scope

Facts may be scoped by market, variant, bundle, package, channel, or revision.

## Derived facts

Example: 6 bottles × 15 mL = 90 mL total.

Mark `DERIVED` and record formula/input fact IDs.
