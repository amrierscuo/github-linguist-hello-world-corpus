# #073 Bluespec

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Simulare una regola Bluespec SystemVerilog che stampa Hello, World! e termina.

Hello.bsv usa il dialetto Bluespec SystemVerilog. La regola invoca $display e $finish; la prova riguarda simulazione Bluesim, non implementazione su FPGA. Binari e file di elaborazione rimangono fuori dal corpus.

## Toolchain e riproduzione

B-Lang BSC 2026.07.1 per Ubuntu 24.04; GNU C++; Tcl 8.6.14 isolato

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bsc -u -sim -g mkHello Hello.bsv
bsc -sim -e mkHello -o hello
```

```text
./hello
```

## Risultato atteso e stato

stdout esatto Hello, World! seguito da newline; simulazione exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://bluespec.dev/bsv-reference/modules-and-interfaces--and-their-instances-rules-in-module-definitions.html
- https://github.com/B-Lang-org/bsc/releases/tag/2026.07.1

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bsv` | [Hello.bsv](Hello.bsv) verificato |
