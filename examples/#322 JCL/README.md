# #322 JCL

Copiare una riga Hello, World! da dati in-stream allo spool SYSOUT con IEBGENER.

Tipo canonico `programming`, language_id `316620079`.

Toolchain prevista: IBM z/OS JES e utility IEBGENER.

Dalla cartella dell’esempio:

```sh
Sottoporre hello.jcl a JES in una coda di prova e leggere SYSUT2.
```

Risultato atteso: step COPY con RC 0; SYSUT2 contiene Hello, World!.

La JOB card è illustrativa: ACCT, CLASS e MSGCLASS dipendono dall’installazione. Non è stato eseguito alcun job su un mainframe.

Stato iniziale: creato; sintassi e semantica in attesa. Ambiente IBM z/OS JES non disponibile.

Fonti:

- [IBM — IEBGENER](https://www.ibm.com/docs/en/zos/3.1.0?topic=utilities-iebgener-sequential-copygenerate-data-set-program)
- [IBM — dati in-stream JCL](https://www.ibm.com/docs/en/zos/3.1.0?topic=statement-dd-data)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jcl` | [hello.jcl](hello.jcl) creato, verifiche pendenti |
