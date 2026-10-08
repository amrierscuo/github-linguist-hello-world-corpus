# #050 B (Formal Method)

Voce canonica: `B (Formal Method)`, tipo `programming`, `language_id: 993355937`.

Definire una macchina Classical B con costante greeting uguale a Hello, World! e operazione hello che restituisce quella costante.

## Toolchain e riproduzione

probcli — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede ProB/probcli o ProB2 UI con parser Classical B. La versione effettiva deve essere registrata quando la toolchain sarà disponibile.

Comando/procedura dalla directory dell’esempio:

```text
ProB2 UI: aprire HelloWorld.mch, eseguire setup dei constants e l’operazione hello, controllare result = "Hello, World!".
```

Risultato atteso: Macchina caricata e tipizzata; operazione hello abilitata e output result esattamente Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Questa voce canonica è il metodo formale B. La macchina non stampa: il saluto è il valore simbolico e il risultato dell’operazione. Nessun parser/animatore B è stato eseguito in questa prova.

Requisiti residui:

- probcli toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://prob.hhu.de/w/index.php?title=Summary_of_B_Syntax](https://prob.hhu.de/w/index.php?title=Summary_of_B_Syntax)
- [https://prob.hhu.de/w/index.php?title=ProB_Cli](https://prob.hhu.de/w/index.php?title=ProB_Cli)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mch` | [HelloWorld.mch](HelloWorld.mch) creato, verifiche pendenti |
