# #301 IDL

Stampare Hello, World! con PRINT in una procedura IDL.

## Toolchain

NV5 Geospatial IDL proprietario; versione da registrare

## Comandi e procedura

IDL> .compile hello.pro
IDL> hello

## Risultato atteso

Console IDL: Hello, World! più newline.

## Stato

Sintassi e semantica in attesa.

IDL è Interactive Data Language, identificato dalla estensione .pro della baseline. La procedura non è CORBA IDL. PRINT e sintassi sono documentati dal vendor.

Requisiti residui:
- Runtime NV5 IDL/licenza non disponibile; compilazione ed esecuzione pending.

## Fonti primarie

- [https://www.nv5geospatialsoftware.com/docs/PRINT.html](https://www.nv5geospatialsoftware.com/docs/PRINT.html)
- [https://www.nv5geospatialsoftware.com/docs/Defining_Procedures.html](https://www.nv5geospatialsoftware.com/docs/Defining_Procedures.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pro` | [hello.pro](hello.pro) creato, verifiche pendenti |
| `.dlm` | [hello.dlm](variants/dlm-86f10b11/hello.dlm) creato, verifiche pendenti |
