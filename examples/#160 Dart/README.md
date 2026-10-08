# #160 Dart

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Analizzare staticamente ed eseguire un programma Dart che stampa Hello, World!.

main usa una variabile final, concatenazione di stringhe e print. La toolchain è lo SDK Dart ufficiale isolato in work; non è necessario Flutter. L’esecuzione usa la VM del medesimo SDK.

## Toolchain e riproduzione

Dart SDK ufficiale 3.13.5 stable, Windows x64

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
dart analyze --fatal-infos hello.dart
dart run hello.dart
```

## Risultato atteso e stato

No issues found; stdout esatto Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://dart.dev/tools/dart-analyze
- https://dart.dev/tools/dart-run

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dart` | [hello.dart](hello.dart) verificato |
