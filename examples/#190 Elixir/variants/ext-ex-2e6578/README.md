# 0190 Elixir: variant `.ex`

Role: Fillable Source Elixir .ex; top-level body uses the same .exs. language

Tipo variante: **alias**. Copia byte-identica di examples/#190 Elixir/hello.exs

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
elixirc -o <output> hello.ex; verificare stdout della valutazione del corpo della unità Elixir.
```

Expected result: exact stdout `Hello, World!\n`, 0. output

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://elixir.hexdocs.pm/introduction.html](https://elixir.hexdocs.pm/introduction.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
