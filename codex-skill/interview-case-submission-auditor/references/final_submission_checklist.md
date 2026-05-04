# Final Submission Checklist

## Package

- Single ZIP or shared folder.
- No nested ZIP.
- No `archive/`.
- No `__pycache__/`.
- No `node_modules/`.
- No raw scratch logs.
- Manifest matches actual files.
- Final ZIP opens with standard tools.

## Dashboard

- One documented launch path.
- Local URL and port are consistent across README, manual, and launcher.
- Normal reviewer mode does not require source rebuild.
- Main pages load:
  - Overview
  - Improvements or Recommendations
  - Details
  - Exception Center
  - Upload or Data Intake
- KPI cards link to row-level evidence.
- Drilldowns show matching row count and extreme values.

## Data And Logic

- Raw files are preserved.
- Cleaned data row count is documented.
- Each issue keeps source file, sheet, row, field, reason, and action.
- Timestamp anomalies are flagged, not silently corrected.
- Capacity checks consider every available capacity dimension.
- Proxy metrics clearly say they are proxies.
- Cost points are not described as actual money unless real rate inputs exist.
- Map distance is not described as road distance unless road network data exists.

## Strategy Document

- 1-3 pages unless the prompt says otherwise.
- Starts with a falsifiable thesis.
- Includes the strongest numbers.
- Separates facts, assumptions, and recommendations.
- Explains limits.
- Includes a phased roadmap when later-stage systems require missing data.

## AI Disclosure

- Names AI role without over-crediting it.
- States human verification path.
- Gives one or two concrete examples of thesis correction or metric tightening.

## Final Search

Search for stale words before shipping:

```text
Problem Data
cost index
avoidable cost
soft-only
Streamlit
old localhost port
route optimizer
real-time dispatch
```

Some terms may be acceptable in a limits section, but they should not contradict the final positioning.
