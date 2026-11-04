# 0186 EdgeQL: variant `.esdl`

Role: Scheme ESDL with Greeting type and default of the message property, not EdgeQL query.

Type: **adapted**. Starting model: examples/#186 EdgeQL/hello.edgeql; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Gel/EdgeDB in istanza temporanea: applicare lo schema hello.esdl; eseguire insert Greeting; select Greeting.message;
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

- [https://docs.geldata.com/reference/edgeql/select](https://docs.geldata.com/reference/edgeql/select)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.geldata.com/database/datamodel](https://docs.geldata.com/database/datamodel)
