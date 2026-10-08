# #476 Noir

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare Noir e restituire l’array pubblico ASCII che rappresenta Hello, World!.

main restituisce13u8 come output pubblico del circuito; Nargo.toml descrive il package locale. Il saluto è dato tipato del circuito, non un commento o un print estraneo al linguaggio.

## Toolchain e riproduzione

Noir/nargo originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nargo check
```

```text
nargo execute
```

## Risultato atteso e stato

Array pubblico72,101,108,108,111,44,32,87,111,114,108,100,33.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compiler/runtime nargo non preparati.

## Fonti primarie

- https://github.com/noir-lang/noir
- https://noir-lang.org/docs/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nr` | [main.nr](src/main.nr) creato, verifiche pendenti |
