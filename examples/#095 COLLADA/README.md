# #095 COLLADA

Represent in COLLADA 1.4.1 an asset titled Hello, World!, with scene GreetingScene and node HelloWorld without shift; validate XSD and upload the scene.

## Toolchain

Python 3.13.9; pycollada 0.9.3; lxml 6.0.2; Khronos COLLADA 1.4.1 XSD

## Commands and procedure

Download the 1.4.1 schema from the source Khronos indicated below and keep it in
an external tool folder. From the example folder:

```sh
python -m pip install -r requirements.txt
python verify.py /percorso/collada_schema_1_4_1.xsd
```

First lxml validates the document against the complete official scheme; then
pycollada loads it and solves the connection of the scene and the matrix of
Node. Only one XML verification of good training would not be enough.

## Expected result

XSD valid the document; parser COLLADA returns the exact title, active scene GreetingScene, node GreetingNode/name HelloWorld and matrix identity.

## Status

syntax and behavior verified.

The title contains the greeting; the XML names of scene and node are valid NCName identifiers. The data model and transformation occurs, not a 3D. graphic rendering The hash of the official schema downloaded is in the log; the schema is not duplicated in the corpus.

Actual verification of 2026-10-08T11:35:41.649498+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://www.khronos.org/collada/](https://www.khronos.org/collada/)
- [https://www.khronos.org/files/collada_schema_1_4_1.xsd](https://www.khronos.org/files/collada_schema_1_4_1.xsd)
- [https://pycollada.readthedocs.io/](https://pycollada.readthedocs.io/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dae` | [hello.dae](hello.dae) verified |
