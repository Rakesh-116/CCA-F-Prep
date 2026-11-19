# Claude Code instructions — CCA-F Project 2

## Project purpose

This is a small Python lab for practicing Claude Code workflows and CI/CD safety.

## Architecture

- Keep application code in `src/` and tests in `tests/`.
- Use the Python standard library unless a requirement explicitly needs a dependency.
- Make small, focused changes. Do not add a framework for one-off behavior.

## Coding conventions

- Target Python 3.11+ and use type hints for public functions.
- Prefer clear names and small functions.
- Do not silently swallow exceptions.
- Do not edit generated files or credentials.

## Verification

Before saying work is complete, run:

```powershell
python -m unittest discover -s tests -t . -v
```

Add or update a test for behavior changes. Report the exact command and outcome.

## Safety boundaries

- Ask before deleting files, changing dependencies, publishing, pushing, or modifying CI secrets.
- Never print, commit, or request secret values.
- In CI, analyze and report by default; do not make repository changes unless the workflow explicitly grants that authority.

## Workflow

For a feature larger than a one-file change: inspect relevant files, state a short plan, wait for approval, then implement and test.
