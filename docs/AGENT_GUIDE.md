# Agent guide

This corpus helps agents locate small language examples, understand their native toolchains and distinguish recorded checks from pending work. It also measures actual GitHub Linguist recognition. It is a private experiment; no GitHub Pages publication is enabled.

## Reference and identifiers

`reference/languages.yml` is the exact supplied snapshot with 836 entries. Its SHA-256 is `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`. The upstream commit and publication date of that snapshot are unknown. Do not replace it with the latest upstream YAML.

| Identifier | Meaning | APL example |
| --- | --- | --- |
| `ordinal` | Stable position in this corpus's supplied YAML | `14`, shown as `#014` |
| `name` | Canonical YAML key | `APL` |
| `language_id` | GitHub Linguist's upstream identifier | `6` |
| `folder` | Exact relative path on disk | `examples/#014 APL` |
| `group` | Language that receives grouped GitHub statistics, when present | Separate from a corpus ID |

Folders keep their existing numbering. `F*` and `Pro*C` use `F∗` and `Pro∗C` in folder names for Windows compatibility. Names and paths may contain spaces, Unicode, `#`, apostrophes or shell metacharacters. Quote paths according to the shell, and encode URL fragments when constructing browser links.

## Query locally, including before GitHub search indexing

The lookup CLI needs Python 3.9 or newer and no packages or network. Run it from any working directory using its path. It verifies the frozen reference and binds metadata to the canonical order before returning results.

```sh
python tools/query_corpus.py
python tools/query_corpus.py APL --json
python tools/query_corpus.py "#014" --json
python tools/query_corpus.py --language-id 6 --json
python tools/query_corpus.py --name node --json
python tools/query_corpus.py --extension .h --json
python tools/query_corpus.py --filename Makefile --json
python tools/query_corpus.py --contains lean --json
python tools/query_corpus.py --type programming --status blocked --json
```

With no filters it returns a summary. Exact name searches also accept upstream aliases and ignore case. Extension lookup ignores case and returns every matching canonical entry, retaining each original suffix. `--contains` searches names and aliases. `--type` and `--status` can narrow any lookup. `pending` means syntax or semantics still needs verification; `unverified` means neither has been verified. No match exits with status 1; invalid arguments or inconsistent source metadata fail explicitly. JSON results include `match_count` and `entries`.

Each detailed result includes the exact README and declared file paths, toolchain, build and run/check commands, expected result, sources, status, blockers, existing verification log and verified file hashes. `extension_variants` holds each suffix's own instructions and flags. Some commands describe an IDE action or prerequisite environment. Inspect the README rather than passing such text directly to a shell. Lookup never executes returned commands or downloads runtimes.

For a compact inventory, use [tracking/agent_index.json](../tracking/agent_index.json). It contains one thin record per canonical entry and SHA-256 values for the source trackers and reference CSV. It is derived, not an alternative source of truth. Full commands, sources and logs remain in the existing tracker/example files.

```sh
python tools/query_corpus.py --check-index
python tools/query_corpus.py --write-index
```

`--check-index` detects stale metadata without writing. Use `--write-index` after an authorized tracker edit, then refresh the checksum manifest.

## Understand the states

The imported baseline has 836 entries with artifacts or drafts, 518 syntax-verified main samples and 468 semantically verified main samples. Those totals do not imply all 836 programs run. There are 368 entries with recorded blockers. [tracking/progress.json](../tracking/progress.json) and the lookup summary provide the current counters.

| Field | What it establishes |
| --- | --- |
| `artifact_created` | A declared file exists, possibly a draft, template or container |
| `syntax_verified` | The recorded validator accepted the specified sample/files |
| `semantic_verified` | The recorded run or native semantic check met its declared goal |
| `verification_log` and hashes | Evidence for exact recorded bytes and environment |
| `blockers` | Missing runtime, host, license, resources or unresolved validation |

Read `validation_mode` and `semantic_goal`: a data format may have a parse/render goal rather than print to a console. A container or projectional model is not interchangeable with a textual program. Verification scope and platform matter.

Extension coverage is separately tracked: the baseline has 1737 artifact-bearing pairs out of 1749 language/extension pairs. A byte-identical alias file is still pending its own check if the extension record says so. Some languages have no extensions and are recognized through filenames or other rules.

## Make a reviewable improvement

1. Query the target and read its README, tracker notes, blockers and primary sources.
2. Install or select the recorded toolchain only when needed and authorized. Keep runtime installations and build outputs outside tracked artifacts.
3. Edit the smallest appropriate example or variant. Preserve canonical IDs, folders and the frozen reference.
4. Run a meaningful syntax/semantic check in its stated environment. Save actual outputs, command, version, UTC timestamp, platform and SHA-256 values. State any partial success or blocker accurately.
5. Update the affected language and extension records consistently. Regenerate the relevant derived files, then the agent index and checksum manifest.
6. Run the audits and review the diff, including attribution, privacy and statistics exclusions.

When extension records have changed, refresh their counters first:

```sh
python tools/extension_coverage.py refresh
```

Then refresh the index and manifest and run both audits:

```sh
python tools/query_corpus.py --write-index
python tools/query_corpus.py --check-index
python tools/corpus.py refresh
python tools/corpus.py audit
python tools/extension_coverage.py audit
```

The audits verify references, declared files, flags, hashes, counters and manifest integrity. They do not rerun hundreds of toolchains and are not a replacement for an edited sample's native check.

## GitHub recognition and byte statistics

There are 563 programming, 71 markup, 184 data and 18 prose entries. Programming/markup supply 634 default candidates; the snapshot's groups aggregate those into 578 theoretical names. GitHub's actual detected names are a separate observation and can differ with its deployed Linguist version, shared suffixes, grouping and exclusions.

The frozen pre-experiment API observation recorded 569 languages and 259622 bytes at source commit `05dfed82885e7a03369f8d1b8a30a84831cf1e70`. Its complete result is [tracking/github_languages_baseline.json](../tracking/github_languages_baseline.json). After the separately requested [Lean share experiment](../experiments/lean-share/README.md), the recorded API measurement is 569 languages, 273213 bytes and 13966 Lean bytes, or 5.11176%. The experiment's [metadata](../experiments/lean-share/experiment.json) gives its timestamp and source commit. Treat these as dated observations; query the API for the current state. The [current measurement after the resumed batch](../tracking/GITHUB_CURRENT.md) records 575 detected names and 5.10875% Lean. The full API response is [github_languages_current.json](../tracking/github_languages_current.json).

```sh
gh api repos/amrierscuo/github-linguist-hello-world-corpus/languages
gh api repos/amrierscuo/github-linguist-hello-world-corpus --jq '{private, default_branch, has_pages}'
```

Authenticated access is needed for this private repo. Do not extract or publish a token. Languages reports bytes, not LOC. The compact sidebar shows a few names and `Other`; the API returns all detected names. GitHub code-search indexing is separate from these byte statistics and can lag after a push. Local lookup works while web search is still indexing.

`.gitattributes` allows the actual source corpus under `examples/` to participate despite Linguist's default documentation rule for that folder. It excludes documentation, helper tools, tracker/index metadata and verification logs. Data/prose retain their default behavior. Do not count helper code toward the collection or use false `linguist-language` labels. Keep `experiments/lean-share/` outside the canonical 836 entries and their verification counters.

Further detail: [tracking/GITHUB_STATS.md](../tracking/GITHUB_STATS.md).

## Reuse, attribution and private assets

No overall license has been chosen for the new corpus material. The MIT license in [LICENSES/GitHub-Linguist-MIT.txt](../LICENSES/GitHub-Linguist-MIT.txt) applies to the imported Linguist reference; it does not automatically license the whole collection. Third-party adaptations retain their own licensing and provenance within the example folders. Review the relevant example's sources and license before reuse.

Research logos, Windows folder icons and the image-based HTML catalog are excluded from this GitHub export. Found originals remain in the separate local corpus. Even a permitted logo must not be introduced here without a separate request to change this export's scope. Official provenance alone does not grant redistribution permission. Keep this repo private and GitHub Pages disabled until the human user explicitly requests publication.
