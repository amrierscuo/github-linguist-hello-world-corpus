# #502 OpenCL

Voce canonica OpenCL; sorgente originale del corpus.

## Obiettivo

Il kernel scrive i13 byte ASCII di Hello, World! nel buffer output usando global ID da0 a12.

## Toolchain e riproduzione

Clang18 originale, versione esatta/provenienza e SHA del compilatore nel log. Dipendenze isolate in work.

```text
clang -x cl -cl-std=CL1.2 -fsyntax-only hello.cl
```

## Risultato atteso e stato

Frontend OpenCL accetta il sorgente con exit0. La prova verifica grammatica, tipi e builtin OpenCL C1.2. Il risultato atteso dal kernel è il buffer contenente Hello, World!; runtime/device e dispatch del kernel restano da verificare.

verification/clang.json contiene comando effettivo, versione, exit/stdout/stderr e SHA-256 del sorgente. Nessun codice GPU è stato eseguito.

## Fonti primarie

- https://clang.llvm.org/docs/UsersManual.html#opencl-features
- https://registry.khronos.org/OpenCL/specs/1.2/pdf/OpenCL_C.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cl` | [hello.cl](hello.cl) sintassi verificata |
| `.opencl` | [hello.opencl](variants/opencl-1927a002/hello.opencl) sintassi verificata |
