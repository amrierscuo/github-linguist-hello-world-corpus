# #638 SRecode Template

Voce e ordine canonici di `reference/languages.yml`.

Caricare un template SRecode e inserire Hello, World!.

## Toolchain e riproduzione

GNU Emacs 29.3 + bundled SRecode. Eseguire dalla cartella dell'esempio:

```sh
emacs -Q --batch --script verify.el
```

Il checker abilita Semantic, compila hello.srt con srecode-compile-file e inserisce file:greeting con srecode-insert. Controlla il testo prodotto dalla risoluzione del dizionario AUDIENCE.

`-Q` disabilita la configurazione personale di Emacs. La prova si esegue in batch.

## Stato e prova

Sintassi e semantica verificate il `2026-10-08T23:33:35.675753+00:00`. Risultato reale: `Hello, World!`.

[Log della verifica](verification/runtime.json) con comandi, versioni, output, exit code e SHA-256 dei file effettivamente controllati.

## Fonti primarie

- [https://raw.githubusercontent.com/emacs-mirror/emacs/master/etc/srecode/default.srt](https://raw.githubusercontent.com/emacs-mirror/emacs/master/etc/srecode/default.srt)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.srt` | [hello.srt](hello.srt) sintassi e semantica verificate |
