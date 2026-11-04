# #001 1C Enterprise

`hello.os` prints `Hello, World!` to the console. The example uses OneScript, an independent implementation of 1C's BSL language. The `.os` extension is listed in the canonical entry; its name and Linguist metadata are unchanged.

## Toolchain and commands

OneScript **2.2.0**, official Windows x64 portable archive. Extract runtime
in a separate folder and make `oscript.exe` available. From the example directory:

```powershell
oscript -check hello.os
oscript hello.os
```

You do not need a separate compilation. The first command must end with code
0 and `No errors.`; the second with 0 code and a single `Hello, World!` line.

## Status and limitations

Syntax **verified** and behavior **verified** with OneScript 2.2.0 on Windows
x64. Effective recording, commands, output codes and source hash
are in `verification/onescript.json`. The runtime used is isolated in the folder
work outside the corpus and is not included in the examples.

This evidence covers the OneScript compatible dialect. It is not a verification
performed on the 1C:Enterprise commercial platform or on its application API.

## Primary sources

- [Progetto OneScript: linguaggio e `Сообщить`](https://www.oscript.io/).
- [Tutorial ufficiale: esecuzione con `oscript file.os`](https://www.oscript.io/learn/tutorial-info).
- [Release ufficiale e archivio portabile 2.2.0](https://github.com/EvilBeaver/OneScript/releases/tag/v2.2.0).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bsl` | [hello.bsl](variants/ext-bsl-2e62736c/hello.bsl) created; verification pending |
| `.os` | [hello.os](hello.os) verified |
