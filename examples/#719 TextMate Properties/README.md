# #719 TextMate Properties

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Upload a TextMate property containing Hello, World!.

Fixtures .tm_properties original with glob selector and string value; the file is not installed in the editor configuration.

## Toolchain and reproduction

TextMate2 originale su macOS, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
TextMate: aprire un file .txt nel progetto e leggere GREETING dalle variabili di un comando bundle
```

## Expected result and status

GREETING = Hello, World! for files * .txt.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: TextMate/macOS not available; property parser and actual hanging variable.

## Primary sources

- https://macromates.com/textmate/manual/settings
