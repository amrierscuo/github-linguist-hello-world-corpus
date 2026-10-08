# #350 KCL

Voce canonica `KCL`, tipo `programming`, language_id `1052003890`.

Definire uno schema KCL con attributi tipizzati e valutare una configurazione che interpola name.

## Toolchain e riproduzione

Official KCL configuration language compiler/evaluator — kcl version 0.13.0-windows-amd64. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

CLI KCL ufficiale 0.13.0 portable Windows x64 dal repository kcl-lang/cli. Questo è KCL di kcl-lang, linguaggio di configurazione CNCF.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
kcl run hello.k
```

Risultato atteso: Configurazione valutata con i due attributi esatti; exit 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compiler autentico controlla schema e tipi e produce YAML con greeting.name=World e greeting.message=Hello, World!. Un reader YAML esistente serve solo a confrontare il prodotto della vera esecuzione KCL.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.kcl-lang.io/docs/reference/lang/spec/schema](https://www.kcl-lang.io/docs/reference/lang/spec/schema)
- [https://github.com/kcl-lang/cli](https://github.com/kcl-lang/cli)
- [https://www.kcl-lang.io/](https://www.kcl-lang.io/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.k` | [hello.k](hello.k) verificato |
