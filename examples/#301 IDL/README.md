# #301 IDL

Print Hello, World! with PRINT in a IDL procedure.

## Toolchain

NV5 Geospatial IDL proprietario; versione da registrare

## Commands and procedure

IDL> .compile hello.pro
IDL> hello

## Expected result

IDL console: Hello, World! plus newline.

## Status

Syntax and behavioral verification pending.

IDL is Interactive Data Language, identified by the .pro extension of the baseline. The procedure is not CORBA IDL. PRINT and syntax are documented by the vendor.

Remaining requirements:
- Runtime NV5 IDL/licenza unavailable; compilazione ed esecuzione pending.

## Primary sources

- [https://www.nv5geospatialsoftware.com/docs/PRINT.html](https://www.nv5geospatialsoftware.com/docs/PRINT.html)
- [https://www.nv5geospatialsoftware.com/docs/Defining_Procedures.html](https://www.nv5geospatialsoftware.com/docs/Defining_Procedures.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pro` | [hello.pro](hello.pro) created; verification pending |
| `.dlm` | [hello.dlm](variants/dlm-86f10b11/hello.dlm) created; verification pending |
