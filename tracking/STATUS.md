# Current corpus status

| Coverage | Status |
| --- | ---: |
| Canonical entries with artifacts or drafts | 836 / 836 |
| Entries with syntax verified for the main sample | 549 / 836 |
| Entries with semantics verified for the main sample | 522 / 836 |
| Language and extension pairs with files | 1738 / 1749 |
| Distinct extensions with primary artifacts | 1480 / 1489 |
| Pairs still missing an artifact | 11 |

The 836 entries cover programming languages, data, markup and prose. The 1,749 language and extension pairs count shared suffixes separately.
Extensions are not 836 additional languages, and verifying a language sample does not verify all its variants.

## Five cases with preliminary artifacts

- MiniD and Charity: the snippets supplied by the user are preserved as drafts. Their grammar and runtime have not been validated. Charity is not marked as a working program.
- LabVIEW: XML templates for `.lvproj`, `.lvclass` and `.lvlib`. The graphical VI is missing and must be created in the IDE.
- JetBrains MPS: an adapted official JetBrains sample with a model, language and solution. MPS generation and execution are pending. The Apache-2.0 license is preserved.
- Altium Designer: altiumts0.0.89 accepted four original ASCII files in a round trip with content assertions. Importing and reopening them in Altium and generating Gerber output remain pending.

## Browse the records

- [All extensions and artifacts](EXTENSIONS.md).
- [Extensions still missing an artifact](EXTENSIONS_PENDING.md).
- [Entry catalog](CATALOG.md), [language tracker](languages_tracker.json), [extension tracker](extensions_tracker.json).
- [Language counts](progress.json), [extension counts](extensions_progress.json), [additional checks](RECHECKS.md).

New aliases are byte-identical copies of the corresponding sources. Other variants have content appropriate to their role: header, module, configuration, descriptor or data.
Formats that require native generation retain a documented blocker instead of an empty file or fabricated binary.
Verification flags stay false until a real parser, compiler or consumer passes a recorded check.

The READMEs list the commands. Toolchains, build outputs and caches stay outside the corpus. Logs preserve actual outputs, exit codes, timestamps and hashes; local path prefixes are normalized where noted.
Text-mode capture may normalize CRLF to LF. Changes to verified sources require a new check.

The original YAML reference retains SHA-256 `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`.

Earlier ZIP files and BATCH reports are historical checkpoints. This page and the trackers describe the current corpus.
