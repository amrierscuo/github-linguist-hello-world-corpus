# #764 Web Ontology Language

Voce canonica `Web Ontology Language`, tipo `data`, language_id `394`.

Ontology OWL original serialized in RDF/XML, with a Greeting class and the English label `Hello, World!`.

## Toolchain and reproduction

rdflib / Python 3.13.9, 7.6.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e RDFLib 7.6.0 in ambiente isolato.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! and PASS for class and label in RDF graph.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

RDFLib reads serialization and assertions control triple OWL.Class and rdfs:label with language tag en. The consistency of an ontology by reasoner is not attested: the goal is this small graph and its label.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.w3.org/TR/owl2-primer/](https://www.w3.org/TR/owl2-primer/)
- [https://rdflib.readthedocs.io/en/stable/](https://rdflib.readthedocs.io/en/stable/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.owl` | [hello.owl](hello.owl) verified |
