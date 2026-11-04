# GitHub Languages observation

REST and GraphQL observation from 2026-10-09T09:00:19.237648+00:00, after pushing commit `a664768c794aa6d6a5ded3a412e748c58939fd31`. At that checkpoint the repository was private, GitHub Pages was disabled, and logos were excluded from the export.

GitHub reported **575 of the 578 expected names** and **273374 bytes**. Lean retained 13966 bytes, or 5.10875%.

B4X appeared after an exact override for the genuine B4J module `examples/#051 B4X/Main.bas`. Its shared suffix was not distinguished without the IDE export header. The source, evidence and native checks remained unchanged. See the [B4X diagnosis](B4X_RECOGNITION.json).

ArkTS, Bend and LLVM TableGen were still missing. They appeared on the official main branch, whose YAML matched the supplied reference byte for byte, but were absent from the published v9.7.0 release. Overrides cannot register new names in the service. The Linguist version deployed by GitHub was not confirmed. Reaching 578 depends on the service adopting these names and must be checked again there. No false label or data format was added to change the count.

[REST response](github_languages_current.json), [observed GraphQL colors and IDs](github_catalog_live.json), [mapping of the 578 names](GITHUB_RECOGNITION_TARGETS.json).

The local dashboard shows only aggregated programming and markup names, numbered #001..#578. Data, prose, variants, extensions and checks stay in the technical records. The numbers of the 836 canonical folders do not change. Aggregated statistics do not verify recognition of every individual file.

GraphQL colors and global GitHub IDs were observed from the service. Numeric YAML `language_id` values and catalog numbers serve different purposes. The UI uses a neutral color for `color: null`. The compact bar may group some names under Other. REST and GraphQL do not expose the cache commit.

Sources: [official overrides](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md#detectable), [v9.7.0 release](https://github.com/github-linguist/linguist/releases/tag/v9.7.0), [GraphQL Language object](https://docs.github.com/en/graphql/reference/objects#language).
