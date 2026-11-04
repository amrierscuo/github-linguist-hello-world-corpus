# #688 SuperCollider

The script concatenates two strings and `Hello, World!` prints in the post window of SuperCollider. The `.sc` variant defines a true `CorpusGreeting` class whose `message` method returns the same text.

Canonical type `programming`, language_id `361`.

## Toolchain and reproduction

Tests performed with sclang 3.13.0 and SCClassLibrary of the official Ubuntu noble `1:3.13.0+repack-1ubuntu3` package, in Ubuntu 24.04 WSL2. Toolchain and dependencies are extracted in an isolated work directory; verification uses a normal user.

With SuperCollider installed and from the example folder:

```sh
QT_QPA_PLATFORM=offscreen sclang -D hello.scd
```

For the `.sc` class, add `variants/sc-4a5e9bf6` to an isolated class library and include the toolchain's SCClassLibrary. Set the actual paths to both directories in `class-library.yaml`:

```yaml
includePaths:
  - /percorso/della/SCClassLibrary
  - /percorso/dell/esempio/variants/sc-4a5e9bf6
excludePaths: []
excludeDefaultPaths: true
postInlineWarnings: false
```

Run the driver from the example folder:

```sh
QT_QPA_PLATFORM=offscreen sclang -D -l class-library.yaml verification/run_class.scd
```

The compilation of the library includes `hello.sc`; the driver invokes `CorpusGreeting.message.postln`. Both tests print a `Hello, World!` line and end with exit code 0. No need to start an audio server.

## Status and evidence

syntax and behavior verified separately for `.scd` and `.sc`.

[Log nativo aggiornato](verification/resume_native.json) with real commands, timestamp UTC, stdout/stderr, configurations, versions and SHA256 of official sources and dependencies. In the extracted toolchain, a local `qt.conf` configures the process paths, resources and translations of Qt.

I warning WSL sullo scheduling realtime e sui permessi della directory runtime XDG non impediscono l'uscita 0 dei programmi. La prova riguarda stringhe e metodi della classe; non certifica sintesi audio o accesso a dispositivi. I [precedenti probe](verification/native.json) sono mantenuti come evidenza storica.

## Primary sources

- [String in SuperCollider](https://doc.sccode.org/Classes/String.html)
- [Scrivere classi](https://doc.sccode.org/Guides/WritingClasses.html)
- [LanguageConfig](https://doc.sccode.org/Classes/LanguageConfig.html)
- [Pacchetto ufficiale Ubuntu](https://packages.ubuntu.com/noble/supercollider-language)
- [Deployment QtWebEngine5.15](https://doc.qt.io/archives/qt-5.15/qtwebengine-deploying.html)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.sc` | [hello.sc](variants/sc-4a5e9bf6/hello.sc) syntax and behavior verified |
| `.scd` | [hello.scd](hello.scd) syntax and behavior verified |
