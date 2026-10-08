# #380 Leo

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare Leo e restituire i13byte ASCII di Hello, World! come risultato della transition main.

I circuiti Leo restituiscono dati tipati anziché stampare testo: la transition espone un array di13u8. program.json identifica il programma locale; nessun deploy o transazione di rete è richiesto.

## Toolchain e riproduzione

Leo/Aleo originale; versione da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
leo build
```

```text
leo run main
```

## Risultato atteso e stato

Output array [72u8,101u8,108u8,108u8,111u8,44u8,32u8,87u8,111u8,114u8,108u8,100u8,33u8].

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Compiler/runtime Leo non preparati; build e valutazione locale pendenti.

## Fonti primarie

- https://github.com/ProvableHQ/leo
- https://provable.com/blog/introducing-the-leo-native-testing-framework

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.leo` | [main.leo](src/main.leo) creato, verifiche pendenti |
