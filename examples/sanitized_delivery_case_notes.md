# Sanitized Delivery Case Notes

This example captures reusable lessons from a delivery-operations interview case without raw data or client files.

## Final Insight Shape

The first framing treated planned-vs-actual vehicle mismatch as execution non-compliance. Raw-data validation showed the causal direction was different: many mismatches were field-side downsizes from oversized planned vehicles.

The stronger interpretation became:

- planning was often over-conservative,
- field teams were correcting some oversized plans after commitment,
- a planning-time capacity gate was a better phase-1 recommendation than real-time dispatch.

## Right-Sizing Pattern

Useful sequence:

1. mismatch count,
2. downsize/upsize/unknown direction,
3. low planned utilization with no field-side correction,
4. strict smaller-vehicle feasibility using all available capacity dimensions,
5. blocked rows where one dimension prevents downsize.

This protects the recommendation from a common reviewer attack: "Low CBM does not mean a smaller truck can carry the cartons or pieces."

## Roadmap Pattern

Phase 1: planning-side validation rules supported by current data.

Phase 2: structured exception capture and master-data cleanup.

Phase 3: real-time dispatch, road-distance routing, or cost optimization only after the missing operational inputs exist.
