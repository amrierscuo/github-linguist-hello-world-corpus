# #550 PowerBuilder

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Importare un user object PowerBuilder e mostrare Hello, World! chiamando greet.

Il sorgente esportato .sru definisce un oggetto nonvisuale e una funzione pubblica PowerScript. MessageBox emette il saluto; il valore di ritorno è0.

## Toolchain e riproduzione

Appeon PowerBuilder originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Importare u_hello.sru in una libreria PowerBuilder; istanziare u_hello e chiamare greet().
```

## Risultato atteso e stato

MessageBox mostra Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Ambiente PowerBuilder non preparato; import/compilazione/esecuzione pendenti.

## Fonti primarie

- https://www.appeon.com/system/files/product-manual/powerscript_reference_v2021.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pbt` | [hello.pbt](variants/pbt-c9751eff/hello.pbt) creato, verifiche pendenti |
| `.sra` | [corpus_hello.sra](variants/sra-88988218/corpus_hello.sra) creato, verifiche pendenti |
| `.sru` | [u_hello.sru](u_hello.sru) creato, verifiche pendenti |
| `.srw` | [w_hello.srw](variants/srw-92c044a7/w_hello.srw) creato, verifiche pendenti |
