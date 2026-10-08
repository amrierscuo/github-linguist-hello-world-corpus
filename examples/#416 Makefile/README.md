# #416 Makefile

Eseguire una ricetta Make che stampa il saluto.

Tipo canonico `programming`, language_id `220`.

Toolchain prevista: GNU Make e shell POSIX.

Dalla cartella dell’esempio:

```sh
make --no-print-directory hello
```

Risultato atteso: stdout Hello, World! e LF, exit 0.

La ricetta usa un tab reale e sopprime l’echo del comando. Non produce file fuori dalla cartella.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: GNU Make on Ubuntu 24.04. [Log](verification/result.json). 

Fonti:

- [GNU Make — ricette](https://www.gnu.org/software/make/manual/html_node/Recipes.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mak` | [hello.mak](variants/mak-6cee4e0b/hello.mak) creato, verifiche pendenti |
| `.d` | [hello.d](variants/d-d5992320/hello.d) verificato |
| `.make` | [hello.make](variants/make-902d3503/hello.make) creato, verifiche pendenti |
| `.makefile` | [hello.makefile](variants/makefile-1b7c71d7/hello.makefile) creato, verifiche pendenti |
| `.mk` | [hello.mk](variants/mk-337c4081/hello.mk) creato, verifiche pendenti |
| `.mkfile` | [hello.mkfile](variants/mkfile-b5a501aa/hello.mkfile) creato, verifiche pendenti |
