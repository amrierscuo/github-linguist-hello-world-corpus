# #003 4D

`HelloWorld.4dm` è il sorgente di un metodo di progetto 4D. Il metodo richiama
`ALERT` e mostra `Hello, World!` in una finestra con pulsante OK.

## Toolchain e comandi

Serve l'applicazione **4D** in modalità di sviluppo. Creare un progetto vuoto,
creare il metodo di progetto `HelloWorld` e inserirvi il contenuto del file.
Il solo `.4dm` è un'unità di sorgente: questa cartella non contiene un progetto
4D completo o un database binario.

Comando reale di controllo nell'IDE: `Design > Compiler... > Check Syntax`.
Compilazione opzionale, se abilitata dalla licenza:
`Design > Compiler... > Compile`. Per la verifica semantica, eseguire il metodo
`HelloWorld` tramite l'Explorer o il comando di esecuzione del metodo.

Risultato atteso: nessun errore dal controllo di sintassi e una finestra con il
testo esatto `Hello, World!`. Per integrare il file su disco in un progetto già
esistente, la posizione dei metodi è `Project/Sources/Methods/`.

## Stato e limiti

Artefatto creato; sintassi e semantica **non ancora verificate**. L'applicazione
4D non è disponibile in questa sessione. Le istruzioni di compilazione dipendono
dal progetto host e, per la compilazione nativa, dalla licenza.

## Fonti ufficiali

- [4D, comando `ALERT`](https://developer.4d.com/docs/commands/alert).
- [4D, architettura del progetto e metodi `.4dm`](https://developer.4d.com/docs/Project/architecture).
- [4D, compilazione e `Check Syntax`](https://developer.4d.com/docs/Project/compiler).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.4dm` | [HelloWorld.4dm](HelloWorld.4dm) creato, verifiche pendenti |
