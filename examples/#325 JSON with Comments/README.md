# #325 JSON with Comments

Analizzare JSONC con un commento e leggere il valore greeting.

Tipo canonico `data`, language_id `423`.

Toolchain prevista: Node.js 22 e Microsoft jsonc-parser 3.3.1.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: Hello, World! e LF; nessun errore di parsing.

Il parser reale gestisce il commento: non viene eliminato da un filtro scritto per il corpus.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + jsonc-parser 3.3.1. [Log](verification/result.json). 

Fonti:

- [Microsoft — jsonc-parser](https://github.com/microsoft/node-jsonc-parser)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund jsonc-parser@3.3.1
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jsonc` | [hello.jsonc](hello.jsonc) verificato |
| `.code-snippets` | [hello.code-snippets](variants/code-snippets-18a98354/hello.code-snippets) sintassi verificata |
| `.code-workspace` | [hello.code-workspace](variants/code-workspace-60504b4f/hello.code-workspace) sintassi verificata |
| `.hujson` | [hello.hujson](variants/hujson-c7ee89b5/hello.hujson) sintassi verificata |
| `.sublime-build` | [hello.sublime-build](variants/sublime-build-cf4a4702/hello.sublime-build) sintassi verificata |
| `.sublime-color-scheme` | [hello.sublime-color-scheme](variants/sublime-color-scheme-52edc858/hello.sublime-color-scheme) sintassi verificata |
| `.sublime-commands` | [hello.sublime-commands](variants/sublime-commands-eb214218/hello.sublime-commands) sintassi verificata |
| `.sublime-completions` | [hello.sublime-completions](variants/sublime-completions-3f74c79e/hello.sublime-completions) sintassi verificata |
| `.sublime-keymap` | [hello.sublime-keymap](variants/sublime-keymap-efe31751/hello.sublime-keymap) sintassi verificata |
| `.sublime-macro` | [hello.sublime-macro](variants/sublime-macro-62e2560e/hello.sublime-macro) sintassi verificata |
| `.sublime-menu` | [Context.sublime-menu](variants/sublime-menu-9e2bded6/Context.sublime-menu) sintassi verificata |
| `.sublime-mousemap` | [hello.sublime-mousemap](variants/sublime-mousemap-5c7e903d/hello.sublime-mousemap) sintassi verificata |
| `.sublime-project` | [hello.sublime-project](variants/sublime-project-dc106a6f/hello.sublime-project) sintassi verificata |
| `.sublime-settings` | [hello.sublime-settings](variants/sublime-settings-5a8fd0f7/hello.sublime-settings) sintassi verificata |
| `.sublime-theme` | [hello.sublime-theme](variants/sublime-theme-326b7d81/hello.sublime-theme) sintassi verificata |
| `.sublime-workspace` | [hello.sublime-workspace](variants/sublime-workspace-22c3c51a/hello.sublime-workspace) sintassi verificata |
| `.sublime_metrics` | [hello.sublime_metrics](variants/sublime-metrics-63303d79/hello.sublime_metrics) sintassi verificata |
| `.sublime_session` | [hello.sublime_session](variants/sublime-session-7137cb4a/hello.sublime_session) sintassi verificata |
| `.tsconfig.json` | [hello.tsconfig.json](variants/tsconfig-json-179eb45b/hello.tsconfig.json) sintassi verificata |
