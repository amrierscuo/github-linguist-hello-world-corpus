# #119 Clarion

Mostrare Hello, World! in una finestra di messaggio Clarion e terminare dopo la sua chiusura.

Tipo canonico: `programming`; `language_id`: `59`.

Toolchain prevista: Clarion per Windows di SoftVelocity, IDE e compilatore con licenza. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
Compilare hello.clw come sorgente principale di un progetto PROGRAM nell’IDE Clarion; eseguire il programma prodotto.
```

Risultato atteso: dialogo Windows con titolo Greeting, testo Hello, World! e pulsante OK; chiudendo il dialogo il programma termina.

Le direttive e le istruzioni sono indentate: la colonna iniziale è riservata alle etichette. I testi del Language Reference sono ripubblicati da Clarion Community Help. La verifica richiede l’ambiente proprietario.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Clarion — PROGRAM, testo del Language Reference](https://www.clarion.help/doku.php?id=program_declare_a_program_.htm)
- [Clarion — MESSAGE, testo del Language Reference](https://clarion.help/doku.php?id=message_return_message_box_response_.htm)
- [SoftVelocity — Clarion](https://www.softvelocity.com/clarion.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.clw` | [hello.clw](hello.clw) creato, verifiche pendenti |
