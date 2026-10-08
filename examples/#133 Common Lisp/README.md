# #133 Common Lisp

Voce canonica: `Common Lisp`, tipo `programming`, `language_id: 66`.

Concatenare stringhe Common Lisp e scriverle sullo standard output con format.

## Toolchain e riproduzione

Native SBCL Ubuntu distribution extracted locally — SBCL 2.2.9.debian. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

SBCL 2.2.9.debian dal pacchetto Ubuntu, estratto sotto work senza installazione globale. Per una estrazione locale impostare SBCL_HOME alla directory usr/lib/sbcl del pacchetto.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
sbcl --script hello.lisp
```

Risultato atteso: Exit 0; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il reader e il compilatore SBCL autentici eseguono il form originale. concatenate usa il tipo risultato string; la direttiva ~A di format scrive il contenuto e ~% aggiunge newline.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://www.sbcl.org/manual/#Shebang-Scripts](https://www.sbcl.org/manual/#Shebang-Scripts)
- [https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm](https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm)
- [https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm](https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lisp` | [hello.lisp](hello.lisp), [greeting.lisp](variants/ext-asd-2e617364/greeting.lisp) creato, verifiche pendenti |
| `.asd` | [hello.asd](variants/ext-asd-2e617364/hello.asd) creato, verifiche pendenti |
| `.cl` | [hello.cl](variants/ext-cl-2e636c/hello.cl) creato, verifiche pendenti |
| `.l` | [hello.l](variants/ext-l-2e6c/hello.l) creato, verifiche pendenti |
| `.lsp` | [hello.lsp](variants/ext-lsp-2e6c7370/hello.lsp) creato, verifiche pendenti |
| `.ny` | [hello.ny](variants/ext-ny-2e6e79/hello.ny) creato, verifiche pendenti |
| `.podsl` | [hello.podsl](variants/ext-podsl-2e706f64736c/hello.podsl) creato, verifiche pendenti |
| `.sexp` | [hello.sexp](variants/ext-sexp-2e73657870/hello.sexp) creato, verifiche pendenti |
