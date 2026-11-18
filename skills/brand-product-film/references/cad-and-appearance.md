# CAD and appearance checks

## Geometry evidence

For STEP, use a CAD reader based on a suitable geometry kernel such as Open CASCADE. Python bindings or a desktop CAD application can expose units, assembly structure, bounds and shape validity. A successful read or equal hash only establishes that specific operation.

Record the following when relevant to the requested shots.

- Source file identity, assembly name, units and revision.
- Assembled dimensions and their relationship to the confirmed production dimensions.
- Part count and geometry checks.
- Conversion settings and faces that failed to triangulate.
- The resulting mesh's boundary and non-manifold edges, including any welding tolerance used for diagnosis.

Keep native CAD validity and mesh-conversion results separate. Fine edges can be altered by tessellation and welding. Inspect the affected part before interpreting a diagnostic as a physical geometry defect. Check repairs for volume or shape changes.

For assembly shots, inspect part identities and the real removal or insertion order. A list of CAD solids provides useful structure but does not by itself prove the physical sequence.

## Appearance evidence

Compare the front, side, top, base, outlet, controls and connector against the photos. Check whether the CAD includes production surface details such as a woven cover, spiral relief or machined rings.

Create neutral material studies using the user's photos. Match the color and reflection in context, since exposure and white balance affect the apparent color. Use real geometry for visible silhouettes and deep relief, and shading detail for small pores or machining marks when appropriate.

Track photo-derived dimensions as estimates. Keep confirmed dimensions in configurable parameters. Rebuild or revise the specific parts affected by a dimensional change so that the product's details remain consistent.

A reusable workflow should support both accurate CAD and photo-based modeling. Avoid turning a mismatch observed in one product into a universal requirement to obtain a new CAD file.

