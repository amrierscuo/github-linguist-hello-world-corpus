# #123 Click

Voce canonica: `Click`, tipo `programming`, `language_id: 61`.

Eseguire uno Script attivo Click che emette Hello, World! e arresta il driver userlevel.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede il driver userlevel di The Click Modular Router, compilato dal repository kohler/click con l’elemento standard Script. Nessuna scheda di rete, pacchetto reale o modulo kernel è necessario.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
click hello.click
```

Risultato atteso: Configurazione Click accettata; una riga Hello, World! nello stream di diagnostica Click; driver terminato.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

La voce .click è il linguaggio di configurazione del router modulare. Il file contiene un elemento Script con TYPE ACTIVE, print e stop. Il driver non è disponibile: nessun parser/runtime è attestato.

Requisiti residui:

- Click Modular Router userlevel binary is not available; Script configuration has not been parsed/run.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://github.com/kohler/click](https://github.com/kohler/click)
- [https://github.com/kohler/click/blob/master/elements/standard/script.hh](https://github.com/kohler/click/blob/master/elements/standard/script.hh)
- [https://github.com/kohler/click/blob/master/doc/click.5](https://github.com/kohler/click/blob/master/doc/click.5)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.click` | [hello.click](hello.click) creato, verifiche pendenti |
