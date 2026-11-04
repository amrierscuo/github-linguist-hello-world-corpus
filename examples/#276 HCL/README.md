# #276 HCL

Voce canonica `HCL`, tipo `programming`, language_id `144`.

Read an attribute string HCL2 which contains greeting.

## Toolchain and reproduction

Existing python-hcl2 HCL2 parser, 7.3.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

python-hcl2 7.3.1, parser HCL2 existing with Lark, on Python 3.13.9. Install in a venv or work directory.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python -m pip install python-hcl2==7.3.1; python verify.py hello.hcl
```

Expected result: Exact Dictionary {message: Hello, World! }; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The verification concerns syntax HCL2 and decoding of the literal value message. It is not attributed execution to Terraform provider or evaluation of expressions not present.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md](https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md)
- [https://github.com/amplify-education/python-hcl2](https://github.com/amplify-education/python-hcl2)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hcl` | [hello.hcl](hello.hcl) verified |
| `.nomad` | [hello.nomad](variants/ext-nomad-2e6e6f6d6164/hello.nomad) created; verification pending |
| `.tf` | [hello.tf](variants/ext-tf-2e7466/hello.tf) created; verification pending |
| `.tfvars` | [hello.tfvars](variants/ext-tfvars-2e746676617273/hello.tfvars) created; verification pending |
| `.tofu` | [hello.tofu](variants/ext-tofu-2e746f6675/hello.tofu) created; verification pending |
| `.workflow` | [hello.workflow](variants/ext-workflow-2e776f726b666c6f77/hello.workflow) created; verification pending |
