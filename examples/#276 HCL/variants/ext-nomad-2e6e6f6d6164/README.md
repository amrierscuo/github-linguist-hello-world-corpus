# 0276 HCL: variant `.nomad`

Role: Job HashiCorp Nomad batch with raw_exec task; parsing verification offline before any scheduler.

Type: **adapted**. Starting model: examples/#276 HCL/hello.hcl; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
nomad job validate hello.nomad (offline/istanza temporanea; nessuna esecuzione scheduler effettuata)
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md](https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md)
- [https://github.com/amplify-education/python-hcl2](https://github.com/amplify-education/python-hcl2)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://developer.hashicorp.com/nomad/docs/job-specification](https://developer.hashicorp.com/nomad/docs/job-specification)
