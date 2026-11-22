# #147 Cycript

## Verified on November 22, 2026

The standalone Cycript compiler accepted the original hello.cy and emitted JavaScript. The native runtime ran the original file with JavaScriptCore and the C FFI in an offline WSL sandbox. A copy of the native bridge database declared the libc puts symbol for this standalone build. The invocation returned 0 and printed exactly Hello, World! followed by one newline.

Run `export LD_LIBRARY_PATH="<private-ffi-library>:$LD_LIBRARY_PATH" && cycript -c hello.cy && cycript hello.cy`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Use Cycript's C interoperability to pass the greeting to puts.

The source combines ECMAScript concatenation and the Cycript cast (typedef const char *). The puts call requires libc statements available in the Cycript runtime. The file goes verified in the original engine: Node.js does not interpret this syntax FFI.

## Toolchain and reproduction

Cycript con JavaScriptCore e binding libc, su piattaforma supportata; versione effettiva da registrare

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
cycript hello.cy
```

## Expected result and status

puts emette Hello, World! e newline.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; native parser/compilatore/runtime has not been performed for this item.

Commitments: Cycript/JavaScriptCore with binding C not available in the current environment; parsing and FFI remain pendants.

## Primary sources

- https://www.cycript.org/manual/
- https://www.cycript.org/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cy` | [hello.cy](hello.cy) Syntax and behavior verified |

</details>
