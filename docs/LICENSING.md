# License scope and third-party material

The root [MIT license](../LICENSE) applies to original code, examples, tools and documentation created for this project. It does not relicense imported material or grant trademark rights.

Imported files, adaptations and their notices retain their own conditions. Preserve each example's attribution and any LICENSE or NOTICE file when reusing it. Where an example contains third-party material, consult its README and provenance before reuse; the project MIT license grants no additional rights to that material.

- The frozen GitHub Linguist reference retains [GitHub Linguist's MIT license](../LICENSES/GitHub-Linguist-MIT.txt).
- The JetBrains MPS and Unity adaptations preserve their upstream Apache-2.0 or MIT licenses and notices in their example folders.
- Official logos and marks are excluded from the project MIT license. Only the 16 original assets documented in [the dashboard attribution page](../site/attributions.html) are included in the public dashboard. Each keeps its documented license or usage policy, source, attribution and display conditions. No unapproved research logo or Windows folder icon is included.
- The original Basteleur and Azeret Mono webfonts retain their SIL Open Font License 1.1 and copyright notices in [Basteleur-OFL.txt](../site/fonts/Basteleur-OFL.txt) and [AzeretMono-OFL.txt](../site/fonts/AzeretMono-OFL.txt). They are unmodified and are not relicensed by the project MIT license.
- Lenis 1.3.26 retains its upstream [MIT license and copyright notice](../site/vendor/Lenis-MIT.txt). The dashboard attribution page and [asset source manifest](../site/asset-sources.json) record the original sources, pinned versions and SHA-256 values for the font and motion assets.

The project is independent of GitHub and the language authors. Names and marks identify the relevant technologies and do not imply endorsement.

## Reproducibility

The repository freezes its reference bytes, numbered examples, recorded commands, outputs and hashes. The local audits check recorded integrity; they do not certify that all examples run on every platform or rerun every native toolchain. Pending checks remain explicit in the trackers.

GitHub Pages deploys the committed `site/` directory through [.github/workflows/pages.yml](../.github/workflows/pages.yml). No toolchain download, corpus execution, tracking service or external font is needed to serve the dashboard.
