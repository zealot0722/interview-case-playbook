# Interview Answer Bank

## How Did You Use AI?

I used AI in two roles: implementation acceleration and adversarial critique. Codex helped build and refactor the tool, tests, package, and documentation. Claude was used to challenge the interpretation and look for weak claims. I did not ship model conclusions directly; I re-ran key claims against raw data and corrected the thesis when the data contradicted the first framing.

## Why Not Build Real-Time Dispatch First?

The dataset supports a historical audit and planning-control gate, not real-time dispatch. It lacks stop sequence, driver location, traffic, road network distance, and a row-level rate card. Building a real-time optimizer first would optimize the wrong constraint. Phase 1 should tighten planning-side validation; phase 2 should capture structured exception reasons and clean master data; phase 3 can add dynamic dispatch or route optimization after the missing inputs exist.

## What Makes The Submission More Than BI?

The dashboard is not just vendor counts or vehicle charts. It converts messy Excel into row-level audit evidence, exception reasons, improvement priorities, and future control rules. Main metrics are clickable, and each recommendation can be traced back to delivery rows.

## How Do You Avoid Overclaiming Cost?

Use improvement points when real cost inputs are missing. State that the points are for prioritization, not currency. If lane rates, vehicle costs, hub handling fees, waiting-cost rules, and labor assumptions become available, the same structure can be upgraded into estimated avoidable cost.

## What Is The Main Operating Lesson?

First correct the planning gate. Then capture structured exception reasons. Then clean master data. Only after those steps should the team invest in route optimization or real-time dispatch.
