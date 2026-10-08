# #456 NEON

Voce canonica `NEON`, tipo `data`, language_id `481192983`.

Decodificare un documento NEON con Nette e leggere i campi message e language.

## Toolchain e riproduzione

Official Nette NEON PHP decoder source snapshot — nette/neon 3.5-dev snapshot; PHP 8.3.6 (cli) (built: Sep  2 2026 12:56:02) (NTS). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Sorgente originale nette/neon branch 3.5-dev, PHP CLI 8.3.6; snapshot e SHA del decoder nel log.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
php -n verify.php /path/to/nette-neon hello.neon
```

Risultato atteso: Hello, World! e PASS della mappa esatta.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il decoder Nette autentico produce la mappa attesa; il helper confronta dati e stampa il saluto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://doc.nette.org/en/neon](https://doc.nette.org/en/neon)
- [https://github.com/nette/neon](https://github.com/nette/neon)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.neon` | [hello.neon](hello.neon) verificato |
