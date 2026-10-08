# #783 XC

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare xC per un target XMOS e stampare Hello, World!.

Sorgente xC originale con entry point e IO stdio. Occorre una toolchain/target XMOS; compilare come C con GCC non verificherebbe xC.

## Toolchain e riproduzione

XMOS XTC/xcc con target appropriato, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
xcc -target=<target-XMOS-di-prova> hello.xc -o hello.xe; xsim hello.xe
```

## Risultato atteso e stato

Hello, World! nel terminale del simulatore/target.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: XTC/xcc e target/simulatore XMOS non disponibili; verifiche pendenti.

## Fonti primarie

- https://www.xmos.com/download/XMOS-Programming-Guide-%28documentation%29%28F%29.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xc` | [hello.xc](hello.xc) creato, verifiche pendenti |
