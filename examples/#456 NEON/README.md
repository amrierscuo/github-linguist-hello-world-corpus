# #456 NEON

Voce canonica `NEON`, tipo `data`, language_id `481192983`.

Decode a NEON document with Nette and read the message and language fields.

## Toolchain and reproduction

Official Nette NEON PHP decoder source snapshot — nette/neon 3.5-dev snapshot; PHP 8.3.6 (cli) (built: Sep  2 2026 12:56:02) (NTS). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Original source nette/neon branch 3.5-dev, PHP CLI 8.3.6; snapshot and SHA of the decoder in the log.

Comando/procedura from the directory of the example, unless explicit indications:

```text
php -n verify.php /path/to/nette-neon hello.neon
```

Expected result: Hello, World! and PASS of the exact map.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic Nette decoder produces the waiting map; the helper compares data and prints greeting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://doc.nette.org/en/neon](https://doc.nette.org/en/neon)
- [https://github.com/nette/neon](https://github.com/nette/neon)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.neon` | [hello.neon](hello.neon) verified |
