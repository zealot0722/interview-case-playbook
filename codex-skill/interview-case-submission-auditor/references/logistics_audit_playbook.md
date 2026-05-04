# Logistics Audit Playbook

Use this reference for historical delivery-operation case studies.

## Useful Tables

- Delivery records: actual transactions, planned quantities, vehicle type, vendor, and timestamps.
- Store master: store code, address, geocode, receiving preferences.
- Warehouse or hub master: location, type, geocode.
- Basic info workbook: vehicle capacity, store-to-warehouse mapping, suppliers, hubs, rate references.

## First Questions

- Which fields are actual execution records?
- Which fields are planning-side references?
- Which master data rows are duplicated or conflicting?
- Are timestamps complete and ordered?
- Does every delivery row map to store and vehicle master data?
- Are rate tables numeric and joinable, or only reference tables?

## Vehicle Fit Logic

Start with normalized planned vs actual vehicle type, but do not assume mismatch means field non-compliance.

Classify direction when vehicle capacity is known:

- Downsize: actual vehicle capacity is smaller than planned.
- Upsize: actual vehicle capacity is larger than planned.
- Unknown: either type is missing from vehicle master.

Right-sizing checks should be multi-dimensional:

- CBM
- carton or box count
- PCS or quantity

A low CBM utilization row is only an action candidate when a smaller known vehicle fits all available capacity dimensions.

## Service-Time Logic

Compute:

- wait time = unload start - arrival
- unload time = unload finish - unload start
- dwell time = unload finish - arrival

Negative values and missing timestamps are data-quality issues.

When building bottleneck scores, weight observed larger delays ahead of theoretical delay types unless a strong operational reason says otherwise.

## Network Logic

Use geocode maps to screen anomalies, not to claim road optimization.

If no stop sequence, driver location, traffic data, road network, or travel-time matrix exists, do not recommend a full route optimizer as phase 1.

## Recommendation Pattern

Prefer:

- planning-time validation gates,
- structured exception reason capture,
- master-data cleanup,
- vendor/store scorecards,
- phased route/cost-model upgrades.

Avoid:

- unsupported real-time dispatch claims,
- fake cost savings,
- treating observation signals as hard violations.
