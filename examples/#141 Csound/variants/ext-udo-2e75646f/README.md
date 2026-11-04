# 0141 Csound: variant `.udo`

Ruolo: User-defined opcode Csound incluso nell’orchestra companion.

Type: **adapted**. Starting model: examples/#141 Csound/hello.orc; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
csound -n consumer.orc schedule.sco
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

- [https://csound.com/docs/manual/prints.html](https://csound.com/docs/manual/prints.html)
- [https://csound.com/docs/manual/CommandFlags.html](https://csound.com/docs/manual/CommandFlags.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://csound.com/docs/manual/udo.html](https://csound.com/docs/manual/udo.html)
