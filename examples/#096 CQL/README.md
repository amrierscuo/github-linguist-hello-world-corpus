# #096 CQL

In Cassandra CQL 3 create a greeting table, insert Hello, World! into the id= 1 line and read it with SELECT.

## Toolchain

Apache Cassandra with CQL 3 and cqlsh; use a dedicated development instance. Versions not observed, to be recorded at the verification.

## Commands and procedure

Use a dedicated Cassandra instance on localhost, then:

```sh
cqlsh --version
cqlsh 127.0.0.1 9042 -f hello.cql
```

The file creates keyspace and table if absent, writes the line id= 1 and the law.
SimpleStrategy/replication_factor= 1 describes the case of a single node
local. Record SELECT output, Cassandra version and cqlsh version for
close the verification. No execution was carried out in this tranche.

## Expected result

DDL and INSERT without errors; SELECT returns a line with message= Hello, World!.

## Status

Syntax and behavioral verification pending.

Linguist is Cassandra Query Language: canonical samples contain create_keyspace/alter_table. The program uses a dedicated keyspace hello_world_corpus; it is not Clinical Quality Language. No Cassandra server has been started or contacted during this tranche.

Remaining requirements:
- Casendra and cqlsh not available: DDL, INSERT and SELECT not executed.

## Primary sources

- [https://cassandra.apache.org/doc/latest/cassandra/developing/cql/index.html](https://cassandra.apache.org/doc/latest/cassandra/developing/cql/index.html)
- [https://cassandra.apache.org/doc/latest/cassandra/developing/cql/ddl.html](https://cassandra.apache.org/doc/latest/cassandra/developing/cql/ddl.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/CQL](https://github.com/github-linguist/linguist/tree/main/samples/CQL)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cql` | [hello.cql](hello.cql) created; verification pending |
