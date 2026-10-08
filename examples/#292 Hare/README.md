# #292 Hare

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare Hare ed emettere Hello, World! usando fmt::printfln.

main è esportata, audience è una costante stringa e il formato Hello, {}! sostituisce World. L’operatore ! asserisce il successo dell’IO. La toolchain necessaria comprende i componenti nativi di Hare.

## Toolchain e riproduzione

Hare, harec, backend QBE e assembler/linker; versioni effettive da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
hare build -o hello hello.ha
```

```text
./hello
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Hare/harec e QBE non preparati; compiler e runtime pendenti.

## Fonti primarie

- https://harelang.org/tutorials/introduction/
- https://docs.harelang.org/fmt/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ha` | [hello.ha](hello.ha) creato, verifiche pendenti |
