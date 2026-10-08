# #417 Mako

Compilare un template Mako e sostituire target con World.

Tipo canonico `programming`, language_id `221`.

Toolchain prevista: Python 3.13 e Mako.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: stdout Hello, World! e LF, exit 0.

Il motore genera ed esegue Python dal template; nessun renderer simulato.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + Mako 1.4.3. [Log](verification/result.json). 

Fonti:

- [Mako — manuale](https://docs.makotemplates.org/en/latest/syntax.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install mako==1.4.3
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mako` | [hello.mako](hello.mako) verificato |
| `.mao` | [hello.mao](variants/mao-7fa3a20f/hello.mao) creato, verifiche pendenti |
