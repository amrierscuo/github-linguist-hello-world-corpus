# GitHub Linguist Hello World Corpus

[Open Linguist Dex](https://amrierscuo.github.io/github-linguist-hello-world-corpus/)

Explore GitHub Linguist through small examples and recorded verification evidence. The dashboard lists **578 names**, numbered **#001 through #578**, with search, language colors, and detail views that work on phones. It opens in the full list by default; Compact view shows 60 names per page.

The recorded GitHub observation found **575 names** in the repository language statistics. ArkTS, Bend, and LLVM TableGen are marked separately because they appear in the frozen reference but were absent from that observation. These counts describe the snapshot and the observation.

## Corpus and reproducibility

The **836 canonical entries** follow the order of the frozen [`languages.yml`](reference/languages.yml) snapshot, from `#001 1C Enterprise` to `#836 xBase`. Directory numbers, dashboard numbers, and Linguist language IDs are separate identifiers.

Reference SHA-256: `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`.

The reference contains 563 programming, 71 markup, 184 data, and 18 prose entries. Linguist groups the 634 programming and markup entries into the 578 names in the dashboard. The trackers record extension coverage separately.

| Recorded coverage | Count |
| --- | ---: |
| Canonical entries with an artifact or draft | 836 / 836 |
| Main samples with verified syntax | 573 / 836 |
| Main samples with verified behavior | 546 / 836 |
| Language and extension pairs with a file | 1738 / 1749 |

Latest verification batch: **2026-11-05**. It added 10 main syntax checks, 10 main behavior checks, and 11 separately verified extension pairs. See the [recorded checks](tracking/VERIFICATION_20261105_TARGET546.md) and the [previous batch](tracking/VERIFICATION_20261105_BATCH.md).

Follow the README in each example directory for its commands, expected result, and limitations. An artifact can still be a draft. A syntax check confirms that the stated validator accepts the sample; behavioral verification also checks the intended result. The audits check recorded evidence, file hashes, and counts. Run the individual commands to reproduce an example's result.

[Verification status](tracking/STATUS.md), [verification batch evidence](tracking/RESUME_20261009.md), [extension coverage](tracking/EXTENSIONS.md), [GitHub language statistics](tracking/GITHUB_CURRENT.md).

## Find and verify examples

See [AGENTS.md](AGENTS.md) and the [agent guide](docs/AGENT_GUIDE.md). The [JSON index](tracking/agent_index.json) lists paths, toolchains, commands, evidence, and blockers without relying on GitHub code search.

```sh
python tools/query_corpus.py APL --json
python tools/query_corpus.py --extension .h --json
python tools/query_corpus.py --type programming --status pending --json
python tools/query_corpus.py --check-index
python tools/corpus.py audit
python tools/extension_coverage.py audit
```

The query tool lists commands without running them. Verification of the main sample does not certify its extension variants.

## Dashboard and GitHub language statistics

GitHub Pages serves the static `site/` directory through the [Pages workflow](.github/workflows/pages.yml). The dashboard serves its fonts and scrolling library locally, requires no installation, and respects reduced motion preferences.

GitHub's language statistics count recognized example bytes. The dashboard, documentation, trackers, logs, and support tools are excluded through `.gitattributes`. Data and prose keep their default Linguist behavior. The [Lean share experiment](experiments/lean-share/README.md) targets 5% and is separate from the 836 canonical entries.

## Licensing and attribution

The [MIT license](LICENSE) covers original project material. The [license scope](docs/LICENSING.md) distinguishes original material, imports, and trademarks. The Linguist reference retains its MIT license. Third party adaptations retain their licenses and notices in the relevant directories.

The dashboard includes **16 original logos with documented permissions**. The [attribution page](https://amrierscuo.github.io/github-linguist-hello-world-corpus/attributions.html) records their sources and conditions, along with the font and library licenses. The project MIT license does not cover logos, trademarks, or other third party material.

This project is independent of GitHub and the language authors. Names and logos identify the technologies and do not imply endorsement.
