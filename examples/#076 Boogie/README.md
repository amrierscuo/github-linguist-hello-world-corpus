# #076 Boogie

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Dimostrare che Greeting restituisce lunghezza 13 e i 13 codici ASCII della stringa Hello, World!.

Boogie è un linguaggio di verifica: la semantica qui è la prova delle postcondizioni, non una stampa console. Il programma assegna la lunghezza e ogni elemento della mappa; Z3 dimostra tutte le postcondizioni. Il runner effettivo invoca BoogieDriver.dll con dotnet e il percorso del solver esplicito.

## Toolchain e riproduzione

Boogie 2.15.9.0, .NET 6.0.36, Z3 5.1.0 64-bit

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
boogie /noVerify hello.bpl
boogie /proverOpt:PROVER_PATH=<z3> hello.bpl
```

## Risultato atteso e stato

Parsing e typecheck senza errori; Boogie: 1 verified, 0 errors.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://github.com/boogie-org/boogie
- https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/krml178.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bpl` | [hello.bpl](hello.bpl) verificato |
