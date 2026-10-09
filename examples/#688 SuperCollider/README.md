# #688 SuperCollider

Lo script concatena due stringhe e stampa `Hello, World!` nella post window di SuperCollider. La variante `.sc` definisce una vera classe `CorpusGreeting` il cui metodo `message` restituisce lo stesso testo.

Tipo canonico `programming`, language_id `361`.

## Toolchain e riproduzione

Prove eseguite con sclang 3.13.0 e SCClassLibrary del pacchetto ufficiale Ubuntu noble `1:3.13.0+repack-1ubuntu3`, in Ubuntu 24.04 WSL2. Toolchain e dipendenze sono estratte in una directory di lavoro isolata; la verifica usa un utente normale.

Con SuperCollider installato e dalla cartella dell'esempio:

```sh
QT_QPA_PLATFORM=offscreen sclang -D hello.scd
```

Per la classe `.sc`, aggiungere la cartella `variants/sc-4a5e9bf6` a una class library isolata e includere la SCClassLibrary della toolchain. Il file `class-library.yaml` deve contenere i percorsi reali di queste due directory:

```yaml
includePaths:
  - /percorso/della/SCClassLibrary
  - /percorso/dell/esempio/variants/sc-4a5e9bf6
excludePaths: []
excludeDefaultPaths: true
postInlineWarnings: false
```

Eseguire il driver dalla cartella dell'esempio:

```sh
QT_QPA_PLATFORM=offscreen sclang -D -l class-library.yaml verification/run_class.scd
```

La compilazione della libreria include `hello.sc`; il driver invoca `CorpusGreeting.message.postln`. Entrambe le prove stampano una riga `Hello, World!` e terminano con exit code 0. Non serve avviare un server audio.

## Stato ed evidenza

Sintassi e semantica verificate separatamente per `.scd` e `.sc`.

[Log nativo aggiornato](verification/resume_native.json) con comandi reali, timestamp UTC, stdout/stderr, configurazioni, versioni e SHA256 dei sorgenti e delle dipendenze ufficiali. Nella toolchain estratta, un `qt.conf` locale configura i percorsi di processo, risorse e traduzioni di Qt. I tentativi iniziali e i successivi successi sono conservati.

I warning WSL sullo scheduling realtime e sui permessi della directory runtime XDG non impediscono l'uscita 0 dei programmi. La prova riguarda stringhe e metodi della classe; non certifica sintesi audio o accesso a dispositivi. I [precedenti probe](verification/native.json) sono mantenuti come evidenza storica.

## Fonti primarie

- [String in SuperCollider](https://doc.sccode.org/Classes/String.html)
- [Scrivere classi](https://doc.sccode.org/Guides/WritingClasses.html)
- [LanguageConfig](https://doc.sccode.org/Classes/LanguageConfig.html)
- [Pacchetto ufficiale Ubuntu](https://packages.ubuntu.com/noble/supercollider-language)
- [Deployment QtWebEngine5.15](https://doc.qt.io/archives/qt-5.15/qtwebengine-deploying.html)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.sc` | [hello.sc](variants/sc-4a5e9bf6/hello.sc) sintassi e semantica verificate |
| `.scd` | [hello.scd](hello.scd) sintassi e semantica verificate |
