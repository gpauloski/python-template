---
name: check
description: Run the full local quality gate (prek hooks + tox test matrix) before committing or opening a pull request. Use when asked to "check", "lint", "run CI locally", or verify a change is ready.
---

# Run the local quality gate

Reproduce what CI runs, in order. Stop and report on the first failure.

1. Sync the environment:
   ```bash
   uv sync
   ```
2. Run all pre-commit hooks (Ruff, mypy, typos, complexipy, ...):
   ```bash
   uv run prek run --all-files
   ```
3. Run the test suite (fast path — current interpreter):
   ```bash
   uv run pytest
   ```
4. Optionally run the full matrix and docs build (slower):
   ```bash
   uv run tox
   ```

Report which steps passed/failed. If a hook auto-fixed files, re-stage them and
re-run step 2.
