# #600 Raw token data

Decodificare un dump raw di token Pygments e recuperare il valore del token string.

Tipo canonico `data`, language_id `318`.

Toolchain prevista: Python e Pygments RawTokenLexer.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: un token Literal.String con valore Hello, World!.

La voce canonica Raw token data è ampia e non definisce uno schema nel seed. L’esempio sceglie esplicitamente il formato raw token documentato da Pygments; la verifica vale per questa variante.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + Pygments RawTokenLexer. [Log](verification/result.json). 

Fonti:

- [Pygments raw token format](https://pygments.org/docs/formatters/#RawTokenFormatter)
- [RawTokenLexer](https://github.com/pygments/pygments/blob/master/pygments/lexers/special.py)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install pygments
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.raw` | [hello.raw](hello.raw) verificato |
