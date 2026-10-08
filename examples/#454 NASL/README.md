# #454 NASL

Voce canonica `NASL`, tipo `programming`, language_id `171666519`.

Eseguire soltanto display del saluto in un script NASL locale.

## Toolchain e riproduzione

Authentic Greenbone OpenVAS NASL interpreter — openvas-nasl 22.7.9; ; Copyright (C) 2002 - 2004 Tenable Network Security; Copyright (C) 2022 Greenbone Networks GmbH. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Interprete Greenbone OpenVAS NASL 22.7.9 estratto localmente con librerie native. Il runtime richiede il suo contesto Redis locale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
openvas-nasl -X hello.nasl
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Non sono presenti primitive di scansione o target esterni. Lo strumento autentico parte, ma il contesto Redis manca: parsing/esecuzione non vengono attestati.

Requisiti residui:

- The genuine Greenbone runtime requires a local Redis KB context that is not configured; execution remains pending.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/greenbone/openvas-scanner](https://github.com/greenbone/openvas-scanner)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nasl` | [hello.nasl](hello.nasl), [driver.nasl](variants/inc-dd126fb7/driver.nasl) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
