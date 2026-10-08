# #799 YASnippet

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Espandere uno snippet YASnippet con il default World.

Lo snippet usa metadata, placeholder1 World e uscita0; richiede il vero parser/expander YASnippet.

## Toolchain e riproduzione

GNU Emacs con YASnippet originale, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Emacs: aprire hello.yasnippet in snippet-mode e usare M-x yas-tryout-snippet
```

## Risultato atteso e stato

Testo espanso Hello, World! con placeholder World selezionato.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Emacs/YASnippet non disponibili; espansione nativa pendente.

## Fonti primarie

- https://joaotavora.github.io/yasnippet/snippet-development.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.yasnippet` | [hello.yasnippet](hello.yasnippet) creato, verifiche pendenti |
