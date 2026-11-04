# #138 Cpp-ObjDump

Voce canonica: `Cpp-ObjDump`, tipo `data`, `language_id: 70`.

Produce an authentic dump GNU objdump of an executable C++ Hello World, keeping disassembly main and byte sections.

## Toolchain and reproduction

GNU G++ and GNU objdump genuine C++ ELF disassembly, GNU objdump ( GNU Binutils for Ubuntu) 2.42. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

GNU G++ 13.3.0 and Binutils objdump/strings 2.42 on Ubuntu 24.04 x86_64. hello.cpp is the source source source; hello.cppobjdump is the real output of the tool and is the canonical data entry. Run from the build directory with a relative short track name to avoid personal paths

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
In una directory build isolata: g++ -std=c++17 -O0 <example>/hello.cpp -o hello; objdump -drwC -s hello > hello.cppobjdump; strings -a hello; ./hello
```

Expected result: Dump ELF x86_64 with <main>: and .rodata section; strings identifies Hello, World!; the executable ends 0 with greeting.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Cpp-ObjDump è un formato di dati generati. Sintassi positiva indica generazione nativa del formato; semantica positiva associa il dump alla vera compilazione, al simbolo main, alla stringa incorporata e alla esecuzione del binario. Il binario non è incluso nel corpus. Gli indirizzi e l’ordine delle sezioni possono differire con compilatori diversi.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)
- [https://sourceware.org/binutils/docs/binutils/strings.html](https://sourceware.org/binutils/docs/binutils/strings.html)
- [https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html](https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cppobjdump` | [hello.cppobjdump](hello.cppobjdump) verified |
| `.c++-objdump` | [hello.c++-objdump](variants/ext-c-objdump-2e632b2b2d6f626a64756d70/hello.c%2B%2B-objdump) created; verification pending |
| `.c++objdump` | [hello.c++objdump](variants/ext-c-objdump-2e632b2b6f626a64756d70/hello.c%2B%2Bobjdump) created; verification pending |
| `.cpp-objdump` | [hello.cpp-objdump](variants/ext-cpp-objdump-2e6370702d6f626a64756d70/hello.cpp-objdump) created; verification pending |
| `.cxx-objdump` | [hello.cxx-objdump](variants/ext-cxx-objdump-2e6378782d6f626a64756d70/hello.cxx-objdump) created; verification pending |
