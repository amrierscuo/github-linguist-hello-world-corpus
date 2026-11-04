# #786 XML Property List

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze a Property List XML and read Hello, World!.

Document plist1.0 with a dictionary and a string. The plistlib decoder reads the value without downloading the external DTD.

## Toolchain and reproduction

original plistlib of the standard Python library; version in the log

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

Dizionario {greeting: Hello, World!}.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.plist` | [hello.plist](hello.plist) verified |
| `.stTheme` | [hello.stTheme](variants/sttheme-0e334249/hello.stTheme) created; verification pending |
| `.tmCommand` | [hello.tmCommand](variants/tmcommand-e3f4e751/hello.tmCommand) created; verification pending |
| `.tmLanguage` | [hello.tmLanguage](variants/tmlanguage-01c07e1d/hello.tmLanguage) created; verification pending |
| `.tmPreferences` | [hello.tmPreferences](variants/tmpreferences-dbf56f6e/hello.tmPreferences) created; verification pending |
| `.tmSnippet` | [hello.tmSnippet](variants/tmsnippet-e9563c64/hello.tmSnippet) created; verification pending |
| `.tmTheme` | [hello.tmTheme](variants/tmtheme-86bf8af9/hello.tmTheme) created; verification pending |
