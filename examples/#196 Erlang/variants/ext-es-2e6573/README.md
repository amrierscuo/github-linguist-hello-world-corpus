# 0196 Erlang: variant `.es`

Role: Escript Erlang with main/1 runner, distinguished by .erl module with main/0.

Type: **adapted**. Starting model: examples/#196 Erlang/hello.erl; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
escript hello.es
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.erlang.org/doc/system/seq_prog.html](https://www.erlang.org/doc/system/seq_prog.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.erlang.org/doc/apps/erts/escript_cmd.html](https://www.erlang.org/doc/apps/erts/escript_cmd.html)
