# #341 Jinja

Voce canonica `Jinja`, tipo `markup`, language_id `147`.

Compilare un template Jinja parametrico e verificare il saluto per World, Reader e parametro mancante.

## Toolchain e riproduzione

Official Jinja compiler/runtime — jinja2 3.1.6. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Jinja 3.1.6 ufficiale già presente su Python 3.13.9. Environment usa StrictUndefined e keep_trailing_newline=True.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py hello.jinja
```

Risultato atteso: Hello, World! e PASS dei controlli parametrici.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il motore reale compila il template e rende due valori esatti. L’assenza del parametro deve sollevare UndefinedError. Nessun template engine alternativo è usato.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://jinja.palletsprojects.com/en/stable/api/](https://jinja.palletsprojects.com/en/stable/api/)
- [https://jinja.palletsprojects.com/en/stable/templates/](https://jinja.palletsprojects.com/en/stable/templates/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jinja` | [hello.jinja](hello.jinja) verificato |
| `.j2` | [hello.j2](variants/j2-d70c3c7d/hello.j2) creato, verifiche pendenti |
| `.jinja2` | [hello.jinja2](variants/jinja2-dda60d41/hello.jinja2) creato, verifiche pendenti |
