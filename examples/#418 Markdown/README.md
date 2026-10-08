# #418 Markdown

Analizzare Markdown CommonMark e renderizzare il saluto come titolo HTML.

Tipo canonico `prose`, language_id `222`.

Toolchain prevista: Python 3.13 e markdown-it-py.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: HTML <h1>Hello, World!</h1> e LF; stdout saluto e LF.

Il README è documentazione; hello.md è l’artefatto Markdown primario separato.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + markdown-it-py 4.2.0. [Log](verification/result.json). 

Fonti:

- [CommonMark — specifica](https://spec.commonmark.org/0.31.2/)
- [markdown-it-py — motore](https://github.com/executablebooks/markdown-it-py)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install markdown-it-py==4.2.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.md` | [hello.md](hello.md) verificato |
| `.livemd` | [hello.livemd](variants/livemd-1b19eac1/hello.livemd) creato, verifiche pendenti |
| `.markdown` | [hello.markdown](variants/markdown-7e4cc6af/hello.markdown) creato, verifiche pendenti |
| `.mdown` | [hello.mdown](variants/mdown-c553b9ee/hello.mdown) creato, verifiche pendenti |
| `.mdwn` | [hello.mdwn](variants/mdwn-d13c3a39/hello.mdwn) creato, verifiche pendenti |
| `.mkd` | [hello.mkd](variants/mkd-ce2bdbce/hello.mkd) creato, verifiche pendenti |
| `.mkdn` | [hello.mkdn](variants/mkdn-ba8fcdf1/hello.mkdn) creato, verifiche pendenti |
| `.mkdown` | [hello.mkdown](variants/mkdown-f8609122/hello.mkdown) creato, verifiche pendenti |
| `.ronn` | [hello.ronn](variants/ronn-8655d3d6/hello.ronn) creato, verifiche pendenti |
| `.scd` | [hello.scd](variants/scd-4dd9ca08/hello.scd) creato, verifiche pendenti |
| `.workbook` | [hello.workbook](variants/workbook-18c428ee/hello.workbook) creato, verifiche pendenti |
