# #453 Myghty

Voce canonica `Myghty`, tipo `programming`, language_id `239`.

Render a Myghty component with a stated parameter in the args block.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires the Myghty historical engender and a compatible Python version, according to its API Interpreter.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Configurare Myghty Interpreter con component_root della cartella e invocare hello.myt con name=World.
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Componente originale; engine storico non configurato. Il nome è un parametro args e l’espressione lo inserisce nel corpo.

Remaining requirements:

- Historical Myghty template runtime/Python compatibility is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pythonhosted.org/Myghty/documentation.html](https://pythonhosted.org/Myghty/documentation.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.myt` | [hello.myt](hello.myt) created; verification pending |
