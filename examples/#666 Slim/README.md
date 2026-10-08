# #666 Slim

Renderizzare un template Slim con un paragrafo di saluto.

Tipo canonico `markup`, language_id `350`.

Toolchain prevista: Ruby3.2.3 + Slim5.2.2 / Temple0.10.7 / Tilt2.9.0.

Dalla cartella dell’esempio:

```sh
ruby verify.rb
```

Risultato atteso: HTML esatto <p>Hello, World!</p>.

Il testo viene renderizzato dal motore originale.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Ruby 3.2.3 + Slim 5.2.2 + Temple 0.10.7 + Tilt 2.9.0. [Log](verification/result.json). 

Fonti:

- [Slim](https://github.com/slim-template/slim)

Preparazione delle dipendenze in una cartella dedicata:

```sh
gem install slim -v 5.2.2
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.slim` | [hello.slim](hello.slim) verificato |
