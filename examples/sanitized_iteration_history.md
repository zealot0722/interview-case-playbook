# Sanitized Iteration History

This file records the reusable process lessons from a data-case submission.

It is intentionally sanitized:

- no client name,
- no raw file names,
- no raw attachments,
- no full chat transcript,
- no personal or recruiter details.

## Why Keep This History

The most useful part of the project was not the final dashboard alone.

The useful part was the correction loop:

1. form an initial thesis,
2. build evidence,
3. let another reviewer attack the thesis,
4. re-run claims against raw data,
5. correct the causal story,
6. tighten recommendations into verifiable gates,
7. package the result as a runnable reviewer tool.

This pattern should be reused for future interview-case submissions.

## Version Arc

### V1 - Build The Audit Tool

The first version focused on engineering completeness:

- raw Excel intake,
- cleaned delivery data,
- exception log,
- dashboard pages,
- strategy outline,
- local runnable package.

The early risk was that the dashboard could look complete while the business thesis was still too generic.

Lesson:

> A runnable dashboard is necessary, but it is not enough. The thesis must survive raw-data challenge.

### V2 - Move From BI To Control Tower

The project moved away from generic BI charts and toward a delivery-operations audit prototype.

The core framing became:

- planning controls,
- vehicle fit,
- service-time friction,
- master-data governance,
- row-level exception evidence.

Lesson:

> A strong case submission should show what the business should control next, not only what happened.

### V3 - Improve Reviewer Readability

The dashboard language was rewritten from developer-style diagnostics into tool-style explanations.

Bad pattern:

```text
problem / failure mode / soft issue
```

Better pattern:

```text
check result / reason detected / what to do next
```

Metrics were given formulas so a reviewer could understand how they were calculated.

Lesson:

> Every major metric should answer: what it is, how it is calculated, and what action it supports.

### V4 - Rename Proxy Cost Into Improvement Points

The cost proxy was renamed so it would not be mistaken for real money.

The UI shifted from total points and delivery count into:

- average points per row,
- rows to review first,
- largest improvement source,
- top-source concentration.

Lesson:

> When cost inputs are missing, use prioritization points and explicitly say they are not currency.

### V5 - Correct The Causal Thesis

A critical review showed that the original thesis had the causal direction wrong.

The first framing treated planned-versus-actual mismatch as execution non-compliance.

Raw-data validation showed the dominant direction was field-side downsizing from oversized planned vehicles.

The thesis changed from:

```text
field execution is not following the plan
```

to:

```text
planning is often over-conservative, and the field is correcting some plans after commitment
```

Lesson:

> Do not treat mismatch as failure until the direction of mismatch is classified.

### V6 - Add Addressable Scope

The recommendation was tightened from a broad principle into a quantified review scope.

The stronger pattern was:

1. identify low planned utilization,
2. require that the field did not already downsize,
3. treat those rows as planning-time review candidates.

Lesson:

> A recommendation becomes stronger when it includes the immediate addressable scope.

### V7 - Add Multi-Dimensional Feasibility

A stricter review pointed out that low volume alone does not prove a smaller vehicle is feasible.

The rule was split into tiers:

- Tier 1: initial screen based on low planned utilization and no field-side downsize.
- Tier 2: actionable candidate only if a smaller known vehicle fits every available capacity dimension.
- Blocked: keep as monitoring only when another capacity dimension prevents downsize.

Lesson:

> For vehicle or capacity recommendations, feasibility must check all relevant dimensions, not just the easiest one.

### V8 - Add Phased Roadmap And AI Disclosure

The strategy document was upgraded from a list of recommendations into a sequence:

- Phase 1: planning-side validation rules supported by current data.
- Phase 2: structured exception capture and master-data cleanup.
- Phase 3: real-time dispatch, routing, and cost optimization only after missing inputs exist.

AI disclosure was also made concrete:

- AI helped critique and implement.
- Human review re-ran key claims.
- Raw-data validation changed the thesis and tightened the recommendation gate.

Lesson:

> A good roadmap explains why some attractive features should not be built first.

### V9 - Make The Package Reviewer-Friendly

The last iteration focused on reviewer friction:

- setup checker,
- clean ZIP,
- manifest,
- local launch path,
- API checks,
- documentation consistency.

Lesson:

> Submission quality includes the reviewer experience. A strong artifact should run without guessing.

## Reusable Review Questions

Use these before shipping future submissions:

1. Is the main thesis a fact, an interpretation, or an assumption?
2. Can every key number be re-run from raw data?
3. Does any mismatch need direction classification before interpretation?
4. Are capacity recommendations checked across all available dimensions?
5. Are proxy metrics clearly separated from money, SLA, distance, or optimization claims?
6. Does the dashboard let the reviewer click from summary to row-level evidence?
7. Do README, dashboard, strategy document, and package contents use the same names?
8. Does the strategy explain what not to build yet and why?
9. Does the AI disclosure show verification, not just tool usage?

## Interview Story

The useful story is:

```text
I first built the audit tool and an initial thesis.
Then I used AI-assisted critique to attack the interpretation.
When the critique raised a plausible issue, I re-ran the numbers against raw data.
That changed the thesis and narrowed the recommendation.
The final submission was not just AI-generated output; it was an evidence-tested iteration loop.
```

This is the part worth preserving.
