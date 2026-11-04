# 0170 Dotenv: variant `.env`

Role: Dotenv file; .env suffix with the same key/value of the .env.example. model

Tipo variante: **alias**. Copia byte-identica di examples/#170 Dotenv/.env.example

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
dotenv originale: dotenv.parse(readFileSync("hello.env")); verificare la proprietà greeting del modello.
```

Expected result: Item exactly { GREETING: "Hello, World!" }; printed greeting and exit 0.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/motdotla/dotenv#usage](https://github.com/motdotla/dotenv#usage)
- [https://github.com/motdotla/dotenv#parse](https://github.com/motdotla/dotenv#parse)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
