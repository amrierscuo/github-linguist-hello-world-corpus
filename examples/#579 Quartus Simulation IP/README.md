# #579 Quartus Simulation IP

Referenziare un testbench di simulazione in un file SIP Quartus.

## Toolchain

Quartus Prime project Tcl; simulator Verilog

## Procedura

Importare hello.sip nel progetto Quartus e simulare hello_tb.v con il simulatore compatibile.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

MISC_FILE/file join/quartus(sip_path) seguono il formato del campione canonico; il testbench originale è il consumer del riferimento.

Requisiti residui:
- Quartus project reader e simulatore non predisposti.

## Fonti primarie

- [https://www.intel.com/content/www/us/en/docs/programmable/683609/23-1/simulation-files.html](https://www.intel.com/content/www/us/en/docs/programmable/683609/23-1/simulation-files.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/Quartus%20Simulation%20IP](https://github.com/github-linguist/linguist/tree/main/samples/Quartus%20Simulation%20IP)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sip` | [hello.sip](hello.sip) creato, verifiche pendenti |
