# #096 CQL

In Cassandra CQL 3 creare una tabella greetings, inserire Hello, World! nella riga id=1 e leggerlo con SELECT.

## Toolchain

Apache Cassandra con CQL 3 e cqlsh; usare un'istanza di sviluppo dedicata. Versioni non osservate, da registrare alla verifica.

## Comandi e procedura

Usare un'istanza Cassandra di sviluppo dedicata su localhost, poi:

```sh
cqlsh --version
cqlsh 127.0.0.1 9042 -f hello.cql
```

Il file crea keyspace e tabella se assenti, scrive la riga id=1 e la legge.
SimpleStrategy/replication_factor=1 descrive il caso di un singolo nodo
locale. Registrare output SELECT, versione Cassandra e versione cqlsh per
chiudere la verifica. Nessuna esecuzione è stata svolta in questa tranche.

## Risultato atteso

DDL e INSERT senza errori; SELECT restituisce una riga con message=Hello, World!.

## Stato

Sintassi e semantica in attesa.

La voce Linguist è Cassandra Query Language: i campioni canonici contengono create_keyspace/alter_table. Il programma usa un keyspace dedicato hello_world_corpus; non è Clinical Quality Language. Nessun server Cassandra è stato avviato o contattato durante questa tranche.

Requisiti residui:
- Istanza Cassandra e cqlsh non disponibili: DDL, INSERT e SELECT non eseguiti.

## Fonti primarie

- [https://cassandra.apache.org/doc/latest/cassandra/developing/cql/index.html](https://cassandra.apache.org/doc/latest/cassandra/developing/cql/index.html)
- [https://cassandra.apache.org/doc/latest/cassandra/developing/cql/ddl.html](https://cassandra.apache.org/doc/latest/cassandra/developing/cql/ddl.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/CQL](https://github.com/github-linguist/linguist/tree/main/samples/CQL)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cql` | [hello.cql](hello.cql) creato, verifiche pendenti |
