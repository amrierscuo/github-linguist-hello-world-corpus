# #406 M4Sugar

Usare M4Sugar con quote quadre, inizializzazione e diversioni per espandere greeting.

Tipo canonico `programming`, language_id `216`.

Toolchain prevista: GNU Autoconf autom4te con linguaggio M4sugar.

Dalla cartella dell’esempio:

```sh
autom4te --language=M4sugar --no-cache hello.m4
```

Risultato atteso: saluto Hello, World! nell’output; sono ammessi soli spazi/fine riga esterni.

M4 semplice non carica automaticamente M4Sugar: il comando usa autom4te e il linguaggio appropriato.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: GNU Autoconf autom4te + M4Sugar (local extracted packages). [Log](verification/result.json). 

Fonti:

- [GNU Autoconf — M4Sugar](https://www.gnu.org/software/autoconf/manual/autoconf-2.72/html_node/M4sugar.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.m4` | [hello.m4](hello.m4) verificato |
