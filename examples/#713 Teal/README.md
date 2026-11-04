# #713 Teal

Voce canonica `Teal`, tipo `programming`, language_id `719038619`.

Controllare i tipi Teal, generare Lua ed eseguire Hello, World!.

## Toolchain and reproduction

Original tea from the teal-language/tl repository and Lua5.4.6.

The original compiler Teal, Lua 5.4.6 and LuaFileSystem/compat53 modules of the test. Run check/gen and Lua in a temporary copy to hold hello.lua out of the corpus.

```text
tl check hello.tl; tl gen hello.tl; lua hello.lua
```

Expected result: Typecheck and output generation 0; runtime exit 0, stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The original compiler rechecks the types, generates Lua, and Lua5.4 performs the result with exact greeting. Comment and statement typed local distinguish the .tl file from Type Language.

Current evidence: [recognition.json](verification/recognition.json), with a UTC timestamp, native commands, exit codes, stdout/stderr, toolchain details and SHA-256 values for modified sources and drivers. Earlier evidence is retained as history. Expected Linguist classification is distinct from the statistics actually observed on GitHub. This batch applies no language override.

## Primary sources

- https://github.com/teal-language/tl
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.tl` | [hello.tl](hello.tl) syntax and behavior verified |
