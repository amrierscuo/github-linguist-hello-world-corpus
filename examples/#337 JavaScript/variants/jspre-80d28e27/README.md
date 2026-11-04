# 0337: JavaScript: `.jspre`

Role: Source or JavaScript fragment of the ECMAScript subset with console.log; no descriptor or binary format is implied.

Origin: Byte-identical copy of the original corpus source: examples/#337 JavaScript/hello.js.

Required toolchain: Node.js 22.20.0. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
node --check hello.jspre (per suffissi non supportati: leggere il testo via vm.Script); eseguire nello stesso host console/ECMAScript del sorgente
```

Expected result: stdout Hello, World! and LF, 0. output

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- Try limited to Node via stdin: loader/framework owner of suffix not verified.

SHA-256 of variant files:

- `hello.jspre`: `dcc62e4a18325773332e645365de256e46ae08fd1609ff72edd1d7367ed4b632`

Primary sources:

- https://nodejs.org/api/console.html#consolelogdata-args

Additive test actually performed:

Node parsed and executed the original JavaScript via stdin. Stdout contained exactly Hello, World! followed by LF. This does not verify proprietary loaders for the suffix.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: v22.20.0
