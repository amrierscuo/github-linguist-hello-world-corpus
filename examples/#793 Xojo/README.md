# #793 Xojo

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Importare un modulo Xojo che restituisce Hello, World!.

File sorgente testuale del modulo con metodo Greeting e tag del formato Xojo. Il modulo restituisce il valore; il progetto ospitante esegue la stampa.

## Toolchain e riproduzione

Xojo IDE/compiler, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Xojo: importare CorpusGreeting.xojo_code in un progetto Console e chiamare Print(CorpusGreeting.Greeting)
```

## Risultato atteso e stato

CorpusGreeting.Greeting() = Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Xojo IDE/compiler non disponibile; import e chiamata pendenti.

## Fonti primarie

- https://docs.xojo.com/getting_started/using_the_xojo_language/modules.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xojo_code` | [CorpusGreeting.xojo_code](CorpusGreeting.xojo_code) creato, verifiche pendenti |
| `.xojo_menu` | [hello.xojo_menu](variants/xojo-menu-015d9908/hello.xojo_menu) creato, verifiche pendenti |
| `.xojo_report` | [hello.xojo_report](variants/xojo-report-fd23e6c1/hello.xojo_report) creato, verifiche pendenti |
| `.xojo_script` | [hello.xojo_script](variants/xojo-script-6019899e/hello.xojo_script) creato, verifiche pendenti |
| `.xojo_toolbar` | [hello.xojo_toolbar](variants/xojo-toolbar-83916cc0/hello.xojo_toolbar) creato, verifiche pendenti |
| `.xojo_window` | [hello.xojo_window](variants/xojo-window-bcc950b1/hello.xojo_window) creato, verifiche pendenti |
