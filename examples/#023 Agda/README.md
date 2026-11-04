# #023 Agda

Voce canonica: `Agda`, tipo `programming`, `language_id: 12`.
`Hello.agda` defines `main : IO ⊤` and invokes `putLine "Hello, World!"`.
The I/O postulate is connected to the GHC backend via the `FOREIGN` pragmas and
`COMPILE`; la conversione `Text.unpack` passa la stringa Agda a `putStrLn` Haskell.

## Toolchain and reproduction

Required toolchain: **Agda con backend GHC** e **GHC** con il pacchetto `text`.
The documentation consulted is Agda 2.9.0; a working local version must
be installed and recorded before verification can be claimed. The
standard library Agda: si importano soltanto moduli `Agda.Builtin`.
From the directory of this example:

```powershell
agda --version
ghc --version
agda Hello.agda
agda --compile Hello.agda
./Hello.exe
```

On Unix systems the generated executable is invoked as `./Hello`.
Expected result: typecheck and compilation without errors; execution with 0 code and
a row exactly `Hello, World!`.

## Status and evidence

Artefatto created; syntax **in attesa**; behavior **in attesa**.
Missing requirement: `agda` and `ghc` executables are not available in PATH
of the tested environment. Reviewing the structure against the documentation
does not count as type checking. The postulate is an FFI boundary: only compilation
GHC controls Haskell connection; typecheck Agda alone does not prove the I/O. effect

Log: [environment.json](verification/environment.json), which registers only
the availability of tools and SHA-256 of the source.
are normalized according to `path_normalization`; no language execution
is declared.

## Official sources

- [Backend GHC, compilazione e esempio di I/O](https://agda.readthedocs.io/en/latest/tools/compilers.html).
- [FFI, pragmas e mapping String verso Data.Text.Text](https://agda.readthedocs.io/en/latest/language/foreign-function-interface.html).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.agda` | [Hello.agda](Hello.agda) created; verification pending |
