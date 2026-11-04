# #355 KakouneScript

Voce canonica `KakouneScript`, tipo `programming`, language_id `603336474`.

Run a Kakoune script that writes greeting in the buffer debug and save that result by comparison.

## Toolchain and reproduction

Official Kakoune command parser and editor runtime, Kakoune unknown. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Kakoune from the Ubuntu 2022.10.31-2 package. The -version command reports "Kakoune unknown" in the package build; the source is documented by the .deb. archive The dummy terminal avoids an interactive UI.

Comando/procedura from the directory of the example, unless explicit indications:

```text
kak -n -ui dummy -e "source hello.kak; buffer '*debug*'; write build/debug.txt; quit!"
```

Expected result: Debug buffer contains Hello, World!; exit 0.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The parser/runtime real loads the .kak file and performs echo -debug. The saved buffer contains the greeting and the process ends 0; the observed content is kept in the log.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/mawww/kakoune/blob/master/doc/pages/commands.asciidoc](https://github.com/mawww/kakoune/blob/master/doc/pages/commands.asciidoc)
- [https://github.com/mawww/kakoune](https://github.com/mawww/kakoune)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.kak` | [hello.kak](hello.kak) verified |
