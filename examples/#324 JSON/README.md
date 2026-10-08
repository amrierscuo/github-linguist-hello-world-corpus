# #324 JSON

Analizzare JSON e recuperare greeting uguale a Hello, World!.

Tipo canonico `data`, language_id `174`.

Toolchain prevista: Python 3.13 json standard library.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Controllo del formato e del valore effettivo letto dal parser.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 json standard library. [Log](verification/result.json). 

Fonti:

- [RFC 8259 — JSON](https://www.rfc-editor.org/rfc/rfc8259)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.json` | [hello.json](hello.json) verificato |
| `.4DForm` | [hello.4DForm](variants/4dform-f3955d4b/hello.4DForm) sintassi verificata |
| `.4DProject` | [hello.4DProject](variants/4dproject-a665bab0/hello.4DProject) sintassi verificata |
| `.avsc` | [hello.avsc](variants/avsc-c7e061a2/hello.avsc) sintassi verificata |
| `.geojson` | [hello.geojson](variants/geojson-84c738ca/hello.geojson) sintassi verificata |
| `.gltf` | [hello.gltf](variants/gltf-22195b71/hello.gltf) sintassi verificata |
| `.har` | [hello.har](variants/har-efb5fb38/hello.har) sintassi verificata |
| `.ice` | [hello.ice](variants/ice-2db51283/hello.ice) sintassi verificata |
| `.JSON-tmLanguage` | [hello.JSON-tmLanguage](variants/json-tmlanguage-952f6f40/hello.JSON-tmLanguage) sintassi verificata |
| `.json.example` | [hello.json.example](variants/json-example-daa9bfa3/hello.json.example) sintassi verificata |
| `.jsonl` | [hello.jsonl](variants/jsonl-365369f9/hello.jsonl) sintassi verificata |
| `.mcmeta` | [hello.mcmeta](variants/mcmeta-7655486e/hello.mcmeta) sintassi verificata |
| `.sarif` | [hello.sarif](variants/sarif-25ba57b0/hello.sarif) sintassi verificata |
| `.slnlaunch` | [hello.slnlaunch](variants/slnlaunch-08c407db/hello.slnlaunch) sintassi verificata |
| `.tact` | [hello.tact](variants/tact-ef114bf1/hello.tact) sintassi verificata |
| `.tfstate` | [hello.tfstate](variants/tfstate-3256bafa/hello.tfstate) sintassi verificata |
| `.tfstate.backup` | [hello.tfstate.backup](variants/tfstate-backup-0768547c/hello.tfstate.backup) sintassi verificata |
| `.topojson` | [hello.topojson](variants/topojson-b7252d50/hello.topojson) sintassi verificata |
| `.webapp` | [hello.webapp](variants/webapp-26d1f665/hello.webapp) sintassi verificata |
| `.webmanifest` | [hello.webmanifest](variants/webmanifest-d224c2a3/hello.webmanifest) sintassi verificata |
| `.yy` | [hello.yy](variants/yy-d3b03e84/hello.yy) sintassi verificata |
| `.yyp` | [hello.yyp](variants/yyp-2fe8cf30/hello.yyp) sintassi verificata |
