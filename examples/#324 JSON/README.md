# #324 JSON

## Latest recorded verification

Latest extension checks:
- `.jsonl`: Unchanged suffix variant; main example status unchanged. [Evidence](verification/native_20261104_followup_2e6a736f6e6c.json).
- `.tfstate`: Terraform show only, local state file read. No init, apply, providers, or cloud activity. [Evidence](verification/native_20261104_followup_2e74667374617465.json).
- `.tfstate.backup`: Terraform show only, local state file read. No init, apply, providers, or cloud activity. [Evidence](verification/native_20261104_followup_2e746673746174652e6261636b7570.json).

Analizzare JSON e recuperare greeting uguale a Hello, World!.

Canonical type `data`, language_id `174`.

Suggested toolchain: Python 3.13 json standard library.

From the example directory:

```sh
python verify.py
```

Expected result: stdout Hello, World! and LF, 0. output

Control of the format and the actual value read by the parser.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 json standard library. [Log](verification/result.json).

Sources:

- [RFC 8259 — JSON](https://www.rfc-editor.org/rfc/rfc8259)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.json` | [hello.json](hello.json) verified |
| `.4DForm` | [hello.4DForm](variants/4dform-f3955d4b/hello.4DForm) syntax verified |
| `.4DProject` | [hello.4DProject](variants/4dproject-a665bab0/hello.4DProject) syntax verified |
| `.avsc` | [hello.avsc](variants/avsc-c7e061a2/hello.avsc) syntax verified |
| `.geojson` | [hello.geojson](variants/geojson-84c738ca/hello.geojson) syntax verified |
| `.gltf` | [hello.gltf](variants/gltf-22195b71/hello.gltf) syntax verified |
| `.har` | [hello.har](variants/har-efb5fb38/hello.har) syntax verified |
| `.ice` | [hello.ice](variants/ice-2db51283/hello.ice) syntax verified |
| `.JSON-tmLanguage` | [hello.JSON-tmLanguage](variants/json-tmlanguage-952f6f40/hello.JSON-tmLanguage) syntax verified |
| `.json.example` | [hello.json.example](variants/json-example-daa9bfa3/hello.json.example) syntax verified |
| `.jsonl` | [hello.jsonl](variants/jsonl-365369f9/hello.jsonl) syntax and behavior verified |
| `.mcmeta` | [hello.mcmeta](variants/mcmeta-7655486e/hello.mcmeta) syntax verified |
| `.sarif` | [hello.sarif](variants/sarif-25ba57b0/hello.sarif) syntax verified |
| `.slnlaunch` | [hello.slnlaunch](variants/slnlaunch-08c407db/hello.slnlaunch) syntax verified |
| `.tact` | [hello.tact](variants/tact-ef114bf1/hello.tact) syntax verified |
| `.tfstate` | [hello.tfstate](variants/tfstate-3256bafa/hello.tfstate) syntax and behavior verified |
| `.tfstate.backup` | [hello.tfstate.backup](variants/tfstate-backup-0768547c/hello.tfstate.backup) syntax and behavior verified |
| `.topojson` | [hello.topojson](variants/topojson-b7252d50/hello.topojson) syntax verified |
| `.webapp` | [hello.webapp](variants/webapp-26d1f665/hello.webapp) syntax verified |
| `.webmanifest` | [hello.webmanifest](variants/webmanifest-d224c2a3/hello.webmanifest) syntax verified |
| `.yy` | [hello.yy](variants/yy-d3b03e84/hello.yy) syntax verified |
| `.yyp` | [hello.yyp](variants/yyp-2fe8cf30/hello.yyp) syntax verified |
