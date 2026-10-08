# #296 HolyC

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Caricare codice HolyC in TempleOS e stampare Hello, World! con Print.

Il file definisce una funzione U0 e un puntatore U8* al pubblico. Il codice top-level chiama Greeting(), come previsto da HolyC; non usa un main C. Il formato %s viene interpretato dal Print nativo TempleOS.

## Toolchain e riproduzione

TempleOS/HolyC originale; versione effettiva da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Nel terminale TempleOS: #include "hello.hc"
```

## Risultato atteso e stato

Print emette Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: TempleOS e compiler/runtime HolyC non disponibili; nessuna verifica con GCC sostitutivo.

## Fonti primarie

- https://raw.githubusercontent.com/cia-foundation/TempleOS/archive/Doc/HolyC.DD
- https://github.com/cia-foundation/TempleOS/tree/archive

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hc` | [hello.hc](hello.hc) creato, verifiche pendenti |
