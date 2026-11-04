# #772 Win32 Message File

Voce canonica `Win32 Message File`, tipo `data`, language_id `950967261`.

File messaggi Win32 originale: risorsa English 0x409, MessageId 1 e simbolo CORPUS_GREETING, contenente `Hello, World!`.

## Toolchain and reproduction

GNU MinGW binutils / Windows FormatMessageW, GNU windmc ( GNU Binutils) 2.41.90.20240122. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Le tre utility Linux sono x86_64-w64-mingw32-windmc, x86_64-w64-mingw32-windres e x86_64-w64-mingw32-ld di GNU binutils 2.41.90.20240122; nel comando abbreviato usare i loro percorsi assoluti. cpp è il preprocessore GNU locale. Prodotti compilati solo nella directory output esterna; la lettura finale richiede Windows x64.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Linux, dalla directory output esterna: windmc -h . -r . <esempio>/hello.mc
windres --preprocessor=cpp --input hello.rc --output messages.o --output-format coff
ld --dll --entry=0 --output messages.dll messages.o
Windows: powershell -NoProfile -File verify.ps1 -LibraryPath <output>/messages.dll
```

Expected result: Hello, World! bed from FormatMessageW and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

windmc compila il formato .mc, windres genera COFF e ld collega una DLL contenente solo risorse. Windows carica la DLL come dati e FormatMessageW legge il MessageId English: il risultato effettivo è confrontato con il saluto. La DLL non viene installata.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://learn.microsoft.com/en-us/windows/win32/eventlog/message-text-files](https://learn.microsoft.com/en-us/windows/win32/eventlog/message-text-files)
- [https://sourceware.org/binutils/docs/binutils/windmc.html](https://sourceware.org/binutils/docs/binutils/windmc.html)
- [https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-formatmessagew](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-formatmessagew)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mc` | [hello.mc](hello.mc) verified |
