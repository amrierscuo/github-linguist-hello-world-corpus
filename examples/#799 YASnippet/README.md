# #799 YASnippet

Voce e ordine canonici di `reference/languages.yml`.

Espandere uno snippet YASnippet con il default World.

## Toolchain e riproduzione

GNU Emacs 29.3 + original YASnippet 0.14.0. Eseguire dalla cartella dell'esempio:

```sh
emacs -Q --batch --load <YASnippet-0.14.0>/yasnippet.el --load verify.el
```

Installare YASnippet originale 0.14.0 e sostituire il percorso fra parentesi angolari. Il checker usa il parser originale per i metadata, registra lo snippet in text-mode, espande il trigger greeting e verifica testo completo e placeholder 1 World ancora attivo.

`-Q` disabilita la configurazione personale di Emacs. La prova si esegue in batch.

## Stato e prova

Sintassi e semantica verificate il `2026-10-08T23:33:35.865605+00:00`. Risultato reale: `Hello, World!`.

[Log della verifica](verification/runtime.json) con comandi, versioni, output, exit code e SHA-256 dei file effettivamente controllati.

## Fonti primarie

- [https://joaotavora.github.io/yasnippet/snippet-development.html](https://joaotavora.github.io/yasnippet/snippet-development.html)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.yasnippet` | [hello.yasnippet](hello.yasnippet) sintassi e semantica verificate |
