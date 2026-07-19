This guide covers the one-time GitHub configuration for a repository created
from this template.

## Recommended Repository Defaults

In your repository **Settings**:

- **General → Pull Requests:**
    - Prefer **Squash merging** (and consider disabling merge commits) to keep a
      linear history where one PR maps to one commit.
    - Enable **Automatically delete head branches** to clean up merged branches.
- **Branches → Add branch ruleset (or protection) for `main`:**
    - Require a pull request before merging.
    - Require status checks to pass before merging, and require branches to be
      up to date. Select the checks you want to enforce (e.g. `tests`, `prek`,
      `check-docs`).
    - Do not allow bypassing the above settings.
- **Pages:** once the `docs` workflow has run and created the `gh-pages`
  branch, set Pages to deploy from that branch.
- **Actions → General:** allow the workflow permissions the template needs
  (the workflows request least-privilege permissions per job).

## PyPI Trusted Publishing

The `publish` workflow uses
[PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/){target=_blank}
(OIDC), so no API token secret is required. Configure a
[pending publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/){target=_blank}
on PyPI that points at this repository, the `publish.yml` workflow, and the
`release` environment (if you use one).

## Issue and Pull Request Labels

Release notes are generated automatically from PR labels (see
`.github/release.yml`). Create the following labels so the generated changelog
is organized correctly:

| Label | Purpose | Suggested color |
| --- | --- | --- |
| `breaking` | Backwards-incompatible changes | `#b60205` |
| `enhancement` | New features | `#0e8a16` |
| `bug` | Bug fixes | `#d73a4a` |
| `refactor` | Internal changes / improvements | `#fbca04` |
| `documentation` | Documentation-only changes | `#0075ca` |
| `dependencies` | Dependency updates | `#c5def5` |
| `ignore-for-release` | Excluded from release notes | `#ededed` |

Every PR should carry at least one of these labels; unlabeled PRs fall into the
"Other Changes" section of the release notes. You can create them quickly with
the [GitHub CLI](https://cli.github.com/){target=_blank}, e.g.:

```bash
$ gh label create breaking --color b60205 --description "Breaking change"
```
