# #501 OpenAPI Specification v3

Validate a specific OpenAPI v3 with text/plain response and greeting example.

Canonical type `data`, language_id `557959099`.

Suggested toolchain: Python, PyYAML and openapi-spec-validator.

From the example directory:

```sh
python verify.py
```

Expected result: valid OpenAPI scheme and example Hello, World! read from the document.

The verification concerns the API contract and its example; it does not start a HTTP service.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + openapi-spec-validator 0.9.0 + PyYAML. [Log](verification/result.json).

Sources:

- [OpenAPI 3.0.3](https://spec.openapis.org/oas/v3.0.3.html)
- [Validator](https://github.com/python-openapi/openapi-spec-validator)

Install the dependencies in a separate directory:

```sh
python -m pip install openapi-spec-validator PyYAML
```

Install the dependencies in a separate directory:

```sh
python -m pip install openapi-spec-validator==0.9.0 PyYAML
```
