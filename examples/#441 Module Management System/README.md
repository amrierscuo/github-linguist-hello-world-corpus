# #441 Module Management System

Voce canonica `Module Management System`, tipo `programming`, language_id `235`.

Invocare WRITE SYS$OUTPUT da un target del Module Management System OpenVMS.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede OpenVMS e VSI MMS o MMK compatibile, con DCL.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
MMS /DESCRIPTION=descrip.mms HELLO
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Target e azione DCL originali; nessun ambiente OpenVMS disponibile.

Requisiti residui:

- OpenVMS with MMS/MMK is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.vmssoftware.com/docs/vsi-decset-for-openvms-guide-to-the-module-management-system.pdf](https://docs.vmssoftware.com/docs/vsi-decset-for-openvms-guide-to-the-module-management-system.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mms` | [descrip.mms](descrip.mms) creato, verifiche pendenti |
| `.mmk` | [hello.mmk](variants/mmk-3528f1de/hello.mmk) creato, verifiche pendenti |
