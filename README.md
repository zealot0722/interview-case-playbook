# Interview Case Playbook

Private playbook for turning messy data-case assignments into reviewer-facing submissions.

This repo is intentionally reusable and sanitized:

- No raw interview attachments.
- No final submission ZIP files.
- No complete chat transcripts.
- No company-confidential details.

Use it for:

- Codex skill installation.
- GPT knowledge uploads.
- Strategy-document templates.
- Final package verification scripts.

## Layout

```text
codex-skill/
  interview-case-submission-auditor/
    SKILL.md
    references/
    scripts/
gpt-knowledge/
templates/
examples/
```

## Install The Codex Skill

Clone this private repo on each machine, then create a junction:

```powershell
New-Item -ItemType Junction `
  -Path "$env:USERPROFILE\.codex\skills\interview-case-submission-auditor" `
  -Target "<repo>\codex-skill\interview-case-submission-auditor"
```

After updating this repo:

```powershell
git pull
```

## GPT Knowledge

Upload files from `gpt-knowledge/` when you want a GPT to help with:

- interview storytelling,
- reviewer-style critique,
- AI usage disclosure,
- follow-up Q&A preparation.

Do not upload raw datasets or private client files.
