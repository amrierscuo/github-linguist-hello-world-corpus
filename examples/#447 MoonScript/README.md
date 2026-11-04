# #447 MoonScript

Voce canonica `MoonScript`, tipo `programming`, language_id `238`.

Fill out a MoonScript source with interpolation and then execute the generated Lua.

## Toolchain and reproduction

Official MoonScript compiler with LPeg and genuine Lua, MoonScript 0.5.0; Lua 5.4.6 Copyright (C) 1994-2023 Lua.org, PUC -Rio. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

MoonScript 0.5.0 original, LPeg and Lua 5.4.6. The two env values containing; they must be passed as singoli/quotati arguments in the shell.

Comando/procedura from the directory of the example, unless explicit indications:

```text
LUA_PATH=/path/to/moonscript/?.lua;/path/to/moonscript/?/init.lua;; LUA_CPATH=/path/to/lpeg/?.so;; lua5.4 verify.lua hello.moon build/hello.lua
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

La libreria moonscript.base.to_lua autentica genera codice; il runtime Lua lo carica ed esegue. Nessun parser sostitutivo.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://moonscript.org/](https://moonscript.org/)
- [https://github.com/leafo/moonscript](https://github.com/leafo/moonscript)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.moon` | [hello.moon](hello.moon) verified |
