# <Case Name> Operations Audit Tool

This is a reviewer-facing submission for `<case brief>`. It is a historical audit tool, not a generic BI dashboard and not a route optimizer.

## Submission Thesis

`<One falsifiable thesis supported by raw-data numbers.>`

Key numbers:

- `<metric 1>`
- `<metric 2>`
- `<metric 3>`

## What Is Included

- dashboard launcher
- audit pipeline
- frontend/backend source
- processed outputs
- strategy document
- assumptions document
- tests

## Reviewer Workflow

1. Read the strategy document.
2. Run the dashboard.
3. Start from Overview.
4. Drill into Improvements and Details.
5. Use the exception center to inspect row-level evidence.

## How To Read The Metrics

- `<Metric>` = `<formula>`.
- `<Metric>` is used for `<purpose>`.
- `<Metric>` is not `<overclaim to avoid>`.

## Verification

```powershell
python -m py_compile <files>
python -m unittest <tests>
python <audit_script>
```

After starting the dashboard:

```powershell
Invoke-WebRequest http://127.0.0.1:<port>/api/status
```

## Scope And Limits

- `<Limit 1>`
- `<Limit 2>`
- `<Future data needed for phase 2/3>`

## AI Tooling Disclosure

`<Briefly explain AI role, human verification, and one concrete correction caused by re-checking data.>`
