# #595 RUNOFF

Formattare un documento RUNOFF contenente il saluto.

Tipo canonico `markup`, language_id `315`.

Toolchain prevista: Digital Standard Runoff o implementazione compatibile.

Dalla cartella dell’esempio:

```sh
RUNOFF hello.rno
```

Risultato atteso: documento formattato con Hello, World!.

Un renderer Markdown non verifica i comandi RUNOFF.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime RUNOFF storico non disponibile.

Fonti:

- [RUNOFF manual DEC](https://bitsavers.org/pdf/dec/vax/vms/5.0/AA-LA51A-TE_VAX_DIGITAL_Standard_Runoff_Reference_Manual_Apr88.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rnh` | [hello.rnh](variants/rnh-1c39dfc9/hello.rnh) creato, verifiche pendenti |
| `.rno` | [hello.rno](hello.rno) creato, verifiche pendenti |
