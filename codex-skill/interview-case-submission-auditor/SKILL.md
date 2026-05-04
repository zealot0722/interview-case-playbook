---
name: interview-case-submission-auditor
description: Use when preparing, reviewing, or packaging a data-analysis interview case submission with a dashboard, strategy document, code, and ZIP deliverable. Focuses on messy Excel audit, row-level traceability, reviewer-facing narrative, AI-use disclosure, and final package consistency.
---

# Interview Case Submission Auditor

Use this skill when a user is building or reviewing a data-case submission for an interview, especially when the deliverables include a dashboard, strategy document, code, and a final ZIP.

## Operating Standard

Treat the work as a reviewer-facing product, not a one-off notebook.

The submission must answer:

1. What does the data say?
2. Which records support each claim?
3. What assumptions were made?
4. What should the reviewer run first?
5. What should the business do next?

Never ship a thesis that is not re-run against the raw data.

## Workflow

1. **Inventory inputs**
   - List files, sheets, row counts, key columns, and obvious duplicates.
   - Keep raw files untouched.
   - Record missing tables, ambiguous fields, multi-value cells, and invalid tokens.

2. **Build an audit layer**
   - Standardize column names.
   - Preserve source file, sheet, row, field, current value, issue reason, and suggested action.
   - Do not silently fix suspicious timestamps or capacity conflicts; flag them.

3. **Separate issue types**
   - Data quality: missing values, timestamp order, duplicate master data.
   - Master data: missing mapping, unknown vehicle types, missing geocodes.
   - Planning control: planned vs actual mismatch, supplier mismatch, planned route gap.
   - Operational friction: wait time, unload time, recurring constraints.
   - Improvement opportunity: quantifiable review priority, not claimed savings unless cost inputs exist.

4. **Create a reviewer-facing tool**
   - Overview page: few high-level signals.
   - Details page: row-level drilldown and extreme values.
   - Exception center: filterable issues with reasons and next actions.
   - Data intake: sample data plus upload or rerun path.
   - Recommendations: future control rules, not unsupported real-time optimization.

5. **Write a short strategy document**
   - 1-3 pages unless the prompt says otherwise.
   - Lead with a falsifiable thesis.
   - Include key numbers, chart or visual, recommendations, limitations, and phased roadmap.
   - Explain why not to jump into optimization if required data is absent.

6. **Validate final consistency**
   - README, user manual, dashboard labels, API labels, strategy doc, and package manifest must agree.
   - Check that old names, old ports, old framework claims, and stale metrics are gone.
   - Run tests and static checks.
   - Rebuild the final ZIP from a clean output folder.

## Reviewer Lens

Push beyond generic BI:

- Replace "problem rows" with "records to review".
- Replace vague labels with exact rules.
- Show formulas for metrics.
- Make KPI cards clickable to row-level evidence.
- Distinguish hard rules from observation signals.
- Do not overclaim proxy metrics as real cost, road distance, SLA violation, or optimization output.

## AI Usage Disclosure

If AI was used, say how:

- AI critique or implementation support.
- Human-defined analytical frame.
- Raw-data verification of key claims.
- Specific examples where verification changed the thesis or metric.

Do not imply AI conclusions were shipped without validation.

## References

Load only when needed:

- `references/final_submission_checklist.md` for final packaging review.
- `references/logistics_audit_playbook.md` for logistics/data-audit framing.
- `references/ai_usage_disclosure_patterns.md` for disclosure language.

## Scripts

Use `scripts/verify_submission_package.py` when checking a final ZIP or submission folder.
