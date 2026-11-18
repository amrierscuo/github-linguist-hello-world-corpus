# #028 Altium Designer

## Verified on November 18, 2026

The published compatible renderer opened the unchanged original PCB and schematic and drew their greeting. Both generated SVG documents contain the exact label.

Run `node draw.mjs with the pinned npm altiumts release`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

[Earlier evidence](verification/altiumts.json).

<details>
<summary>Earlier instructions and evidence</summary>

The example includes four original files in Altium ASCII formats:

- `Hello.PcbDoc`: a rectangular board outline and `Hello, World!` text on the Top Overlay, 40 mil high with a 6 mil stroke.
- `Hello.SchDoc`: a schematic sheet containing the greeting.
- `Hello.PrjPCB`: a project that references the three included documents.
- `Hello.OutJob`: an output job named after the greeting, with a Gerber generator that references the PCB.

The fields and structure follow the open source `altiumts` parser and serializer. This is an ASCII example intended for import. Reopening it in Altium Designer and producing physical output remain pending.

## Reproduction

With Node.js 20 or later and altiumts 0.0.89, run `node verify.mjs` to parse the models and run the assertions. For native verification, open or import the project in Altium Designer, check the text and documents, then save and reopen it. Run the OutJob only in a temporary copy.

Status: the four files were created. Syntax was verified with altiumts 0.0.89. The exact round trip and the assertions for the greeting and references passed. Native Altium semantics remain unverified. [Log](verification/altiumts.json). The open source parser checks and native verification are separate.

Sources: https://github.com/tscircuit/altiumts ; https://github.com/tscircuit/altiumts/blob/main/tests/project-outjob.test.ts ; https://www.altium.com/documentation/altium-designer/tutorial/creating-project-schematic-document

## Extension coverage

Checks for the main example and its variants are recorded separately.

| Extension | File / status |
| --- | --- |
| `.OutJob` | [Hello.OutJob](Hello.OutJob) Syntax and behavior verified |
| `.PcbDoc` | [Hello.PcbDoc](Hello.PcbDoc) Syntax and behavior verified |
| `.PrjPCB` | [Hello.PrjPCB](Hello.PrjPCB) Syntax and behavior verified |
| `.SchDoc` | [Hello.SchDoc](Hello.SchDoc) Syntax and behavior verified |

</details>
