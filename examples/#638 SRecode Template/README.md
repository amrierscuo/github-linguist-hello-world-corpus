# #638 SRecode Template

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Caricare un template SRecode e inserire Hello, World!.

Il file definisce AUDIENCE, contesto file e template greeting con delimitatori SRecode.

## Toolchain e riproduzione

GNU Emacs con SRecode, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Emacs: caricare hello.srt nel database SRecode; in text-mode inserire file:greeting
```

## Risultato atteso e stato

Testo inserito contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Emacs/SRecode non disponibile; parser e inserimento pendenti.

## Fonti primarie

- https://raw.githubusercontent.com/emacs-mirror/emacs/master/etc/srecode/default.srt

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.srt` | [hello.srt](hello.srt) creato, verifiche pendenti |
