---
name: release
description: Cut a new release by tagging a version and publishing via GitHub, which triggers the PyPI Trusted Publishing and docs-deploy workflows. Use when asked to "make a release", "cut a version", or "publish".
---

# Cut a release

Versioning is derived from git tags via setuptools_scm, and publishing is
automated by `.github/workflows/publish.yml`. See
`docs/contributing/releases.md` for the authoritative process.

1. Confirm `main` is green (CI passing) and decide the version `{VERSION}`
   (semver `major.minor.patch`, optional PEP 440 pre/post/dev suffix).
2. Create and push an annotated, signed tag prefixed with `v`:
   ```bash
   git tag -s v{VERSION} -m "pypkg v{VERSION}"
   git push origin v{VERSION}
   ```
3. Create a GitHub Release from the tag titled `pypkg v{VERSION}`:
   - Official release: use "Generate release notes", set the previous official
     tag as the baseline, add an "Upgrade Steps" section, verify PR labels sort
     the notes correctly, and mark it "latest".
   - Pre-release: skip generated notes and mark it "pre-release".
4. Publishing the release triggers the `publish` workflow, which builds with
   `uv build`, uploads to PyPI via Trusted Publishing, and deploys versioned
   docs with `mike`. Confirm both the PyPI upload and the docs deploy succeeded.

Do not push tags or create releases without explicit confirmation from the user.
