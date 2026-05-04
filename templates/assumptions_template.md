# Assumptions

## Data Interpretation

- `<field>` is treated as `<meaning>`.
- Blank `<field>` means `<assumption>`.
- Multi-value `<field>` is handled by `<method>`.

## Cleaning Rules

- Raw data is not overwritten.
- Invalid tokens are flagged, not deleted.
- Timestamp anomalies are flagged and excluded from duration percentiles.

## Metric Rules

- `<Metric>` = `<formula>`.
- `<Metric>` is used for `<ranking / control / observation>`.
- `<Metric>` is not treated as `<overclaim>`.

## Limitations

- Missing `<data>` prevents `<analysis>`.
- Proxy `<metric>` should be replaced by `<future input>` when available.

## Open Questions

- `<Question for business owner>`
- `<Question for data owner>`
