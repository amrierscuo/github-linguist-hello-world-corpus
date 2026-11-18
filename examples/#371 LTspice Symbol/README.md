# #371 LTspice Symbol

## Verified on November 18, 2026

The compatible LTspice symbol reader loaded the original asset and verified the two pins and the exact Value attribute.

Run `python check.py (spicelib AsyReader)`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Open an original LTspice symbol and display the Hello, World! value.

The artifact is a graphic symbol .asy with window3 for Value. Greeting is a label: this fixture does not define an electric model and is not simulated.

## Toolchain and reproduction

Editor simboli LTspice originale; versione da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
Aprire hello.asy nell’editor simboli LTspice.
```

## Expected result and status

Rettangolo, due pin e attributo Value visibile: Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Impedimenti: LTspice non preparato; parsing e visualizzazione nativi pendenti.

## Primary sources

- https://ez.analog.com/other-products/a/documents/DO22731/symbol-file-ad8611-asy-for-ltspice
- https://www.analog.com/en/resources/technical-articles/ltspice-how-to-import-third-party-models.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asy` | [hello.asy](hello.asy) Syntax and behavior verified |

</details>
