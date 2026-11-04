# #325 JSON with Comments

Analyze JSONC with a comment and read the greeting value.

Canonical type `data`, language_id `423`.

Suggested toolchain: Node.js 22 and Microsoft jsonc-parser 3.3.1.

From the example directory:

```sh
node verify.cjs
```

Expected result: Hello, World! and LF; no parsing error.

The real parser handles the comment: it is not deleted by a filter written for the corpus.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + jsonc-parser 3.3.1. [Log](verification/result.json).

Sources:

- [Microsoft — jsonc-parser](https://github.com/microsoft/node-jsonc-parser)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund jsonc-parser@3.3.1
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jsonc` | [hello.jsonc](hello.jsonc) verified |
| `.code-snippets` | [hello.code-snippets](variants/code-snippets-18a98354/hello.code-snippets) syntax verified |
| `.code-workspace` | [hello.code-workspace](variants/code-workspace-60504b4f/hello.code-workspace) syntax verified |
| `.hujson` | [hello.hujson](variants/hujson-c7ee89b5/hello.hujson) syntax verified |
| `.sublime-build` | [hello.sublime-build](variants/sublime-build-cf4a4702/hello.sublime-build) syntax verified |
| `.sublime-color-scheme` | [hello.sublime-color-scheme](variants/sublime-color-scheme-52edc858/hello.sublime-color-scheme) syntax verified |
| `.sublime-commands` | [hello.sublime-commands](variants/sublime-commands-eb214218/hello.sublime-commands) syntax verified |
| `.sublime-completions` | [hello.sublime-completions](variants/sublime-completions-3f74c79e/hello.sublime-completions) syntax verified |
| `.sublime-keymap` | [hello.sublime-keymap](variants/sublime-keymap-efe31751/hello.sublime-keymap) syntax verified |
| `.sublime-macro` | [hello.sublime-macro](variants/sublime-macro-62e2560e/hello.sublime-macro) syntax verified |
| `.sublime-menu` | [Context.sublime-menu](variants/sublime-menu-9e2bded6/Context.sublime-menu) syntax verified |
| `.sublime-mousemap` | [hello.sublime-mousemap](variants/sublime-mousemap-5c7e903d/hello.sublime-mousemap) syntax verified |
| `.sublime-project` | [hello.sublime-project](variants/sublime-project-dc106a6f/hello.sublime-project) syntax verified |
| `.sublime-settings` | [hello.sublime-settings](variants/sublime-settings-5a8fd0f7/hello.sublime-settings) syntax verified |
| `.sublime-theme` | [hello.sublime-theme](variants/sublime-theme-326b7d81/hello.sublime-theme) syntax verified |
| `.sublime-workspace` | [hello.sublime-workspace](variants/sublime-workspace-22c3c51a/hello.sublime-workspace) syntax verified |
| `.sublime_metrics` | [hello.sublime_metrics](variants/sublime-metrics-63303d79/hello.sublime_metrics) syntax verified |
| `.sublime_session` | [hello.sublime_session](variants/sublime-session-7137cb4a/hello.sublime_session) syntax verified |
| `.tsconfig.json` | [hello.tsconfig.json](variants/tsconfig-json-179eb45b/hello.tsconfig.json) syntax verified |
