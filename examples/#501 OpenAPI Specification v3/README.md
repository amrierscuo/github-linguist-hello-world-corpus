# #501 OpenAPI Specification v3

Validare una specifica OpenAPI v3 con risposta text/plain ed esempio di saluto.

Tipo canonico `data`, language_id `557959099`.

Toolchain prevista: Python, PyYAML e openapi-spec-validator.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: schema OpenAPI valido ed esempio Hello, World! letto dal documento.

La verifica riguarda il contratto API e il suo esempio; non avvia un servizio HTTP.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + openapi-spec-validator 0.9.0 + PyYAML. [Log](verification/result.json). 

Fonti:

- [OpenAPI 3.0.3](https://spec.openapis.org/oas/v3.0.3.html)
- [Validator](https://github.com/python-openapi/openapi-spec-validator)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install openapi-spec-validator PyYAML
```

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install openapi-spec-validator==0.9.0 PyYAML
```
