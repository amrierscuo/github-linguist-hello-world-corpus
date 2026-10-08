# #060 Befunge

Voce canonica: `Befunge`, tipo `programming`, `language_id: 30`.

Emettere i tredici caratteri del saluto dalla pila Befunge-93, aggiungere LF e fermarsi con @.

## Toolchain e riproduzione

Chris Pressey reference Befunge-93 interpreter — 2.25. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Richiede il reference interpreter Befunge-93 v2.25 di Chris Pressey. Compilazione invariata dell’upstream: gcc -O2 -o bef bef.c. Eseguire dalla directory dell’esempio con un nome relativo corto; l’interprete storico ha buffer di percorso limitati.

Comando/procedura dalla directory dell’esempio:

```text
bef -q hello.befunge
```

Risultato atteso: Exit 0; stdout esattamente Hello, World! seguito da LF.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

String mode inserisce i caratteri in ordine inverso; tredici virgole estraggono il saluto. 25* produce ASCII 10, la virgola lo scrive e @ termina. -q disabilita il banner dell’interprete. Sono stati usati il parser/runtime esistenti, non un interprete inventato per il corpus.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://github.com/catseye/Befunge-93](https://github.com/catseye/Befunge-93)
- [https://github.com/catseye/Befunge-93/blob/master/doc/Befunge-93.markdown](https://github.com/catseye/Befunge-93/blob/master/doc/Befunge-93.markdown)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.befunge` | [hello.befunge](hello.befunge) verificato |
| `.bf` | [hello.bf](variants/ext-bf-2e6266/hello.bf) creato, verifiche pendenti |
