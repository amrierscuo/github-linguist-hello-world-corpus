# #035 Apollo Guidance Computer

Rappresentare Hello, World! con 13 parole AGC contenenti codici ASCII numerici; il programma Block II carica il primo codice (H, ottale 00110) nel registro A e rimane nel ciclo HOLD.

## File

- `hello.agc`

## Toolchain e verifica

Virtual AGC yaYUL revisione 2017-06-19, distribuzione Windows 2017-08-31; emulatore yaAGC per la verifica CPU residua.

`OCT` inserisce costanti ottali di 15 bit nella memoria assemblata. Ogni
carattere del saluto occupa una parola: non è una codifica usata storicamente
dal DSKY, ma una convenzione esplicita del campione. `CA GREET` carica H nel
registro A; `TC HOLD` mantiene il controllo in un ciclo.

```text
yaYUL hello.agc
```

Il comando produce `hello.agc.bin` e `hello.agc.symtab` nella cartella di lavoro;
usare una copia temporanea della sorgente per tenere separati questi derivati.
L'assemblatore del test dichiara la revisione 2017-06-19 nella propria intestazione.

Prova CPU ancora richiesta: caricare il core-rope in un'istanza yaAGC Block II,
usare il debugger per impostare il program counter Z a 04000, eseguire `CA`,
osservare A=00110 e il ciclo sul successivo `HOLD`; leggere le tredici parole
da `GREET` come valori ASCII numerici per ricostruire Hello, World!.
Questo protocollo non è stato eseguito e non esiste una prova di stampa.

## Risultato atteso

Assembly exit 0, zero errori fatali e warning. Obiettivo CPU: A=00110 e HOLD ripetuto; codici dati 00110 00145 00154 00154 00157 00054 00040 00127 00157 00162 00154 00144 00041.

## Stato della prova

Sintassi verificata. Semantica in attesa.

Il saluto è una convenzione ASCII esplicita del campione. Assemblaggio completo realmente eseguito, semantica CPU non verificata.

Prova effettiva Windows x64 del 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
Il log include hash SHA-256 della sorgente, versioni osservate, comandi, codici di uscita, stdout e stderr.

Requisiti residui:
- Manca la prova CPU in yaAGC: registro A e ciclo HOLD non osservati. L'AGC non possiede una console di testo; non viene dichiarata alcuna stampa.

## Fonti primarie

- [https://www.ibiblio.org/apollo/assembly_language_manual.html](https://www.ibiblio.org/apollo/assembly_language_manual.html)
- [https://www.ibiblio.org/apollo/yaYUL.html](https://www.ibiblio.org/apollo/yaYUL.html)
- [https://github.com/virtualagc/virtualagc](https://github.com/virtualagc/virtualagc)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.agc` | [hello.agc](hello.agc) sintassi verificata |
