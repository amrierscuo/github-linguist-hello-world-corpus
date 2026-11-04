# #793 Xojo

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Import an Xojo module that returns Hello, World!.

Textual module source file with Greeting method and Xojo format tag. The module returns the value; the host project performs the print.

## Toolchain and reproduction

Xojo IDE/compiler, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Xojo: importare CorpusGreeting.xojo_code in un progetto Console e chiamare Print(CorpusGreeting.Greeting)
```

## Expected result and status

CorpusGreeting.Greeting() = Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Xojo IDE/compiler unavailable; import and call hangings.

## Primary sources

- https://docs.xojo.com/getting_started/using_the_xojo_language/modules.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xojo_code` | [CorpusGreeting.xojo_code](CorpusGreeting.xojo_code) created; verification pending |
| `.xojo_menu` | [hello.xojo_menu](variants/xojo-menu-015d9908/hello.xojo_menu) created; verification pending |
| `.xojo_report` | [hello.xojo_report](variants/xojo-report-fd23e6c1/hello.xojo_report) created; verification pending |
| `.xojo_script` | [hello.xojo_script](variants/xojo-script-6019899e/hello.xojo_script) created; verification pending |
| `.xojo_toolbar` | [hello.xojo_toolbar](variants/xojo-toolbar-83916cc0/hello.xojo_toolbar) created; verification pending |
| `.xojo_window` | [hello.xojo_window](variants/xojo-window-bcc950b1/hello.xojo_window) created; verification pending |
