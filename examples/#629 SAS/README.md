# #629 SAS

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire un DATA step SAS e scrivere Hello, World! nel log.

DATA _NULL_ evita di creare dataset; la stringa ha lunghezza dichiarata13 e PUT scrive il valore calcolato.

## Toolchain e riproduzione

SAS Base, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
sas hello.sas
```

## Risultato atteso e stato

Hello, World! nel log SAS.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: SAS runtime/licenza non disponibile; parser e log di esecuzione pendenti.

## Fonti primarie

- https://support.sas.com/documentation/cdl/en/basess/58133/HTML/default/a002108635.htm

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sas` | [hello.sas](hello.sas) creato, verifiche pendenti |
