# #276 HCL

Voce canonica `HCL`, tipo `programming`, language_id `144`.

Leggere un attributo stringa HCL2 che contiene il saluto.

## Toolchain e riproduzione

Existing python-hcl2 HCL2 parser — 7.3.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

python-hcl2 7.3.1, parser HCL2 esistente con Lark, su Python 3.13.9. Installare in un venv o directory di lavoro.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python -m pip install python-hcl2==7.3.1; python verify.py hello.hcl
```

Risultato atteso: Dizionario esatto {message: Hello, World!}; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La verifica riguarda sintassi HCL2 e decoding del valore letterale message. Non viene attribuita esecuzione a provider Terraform o valutazione di espressioni non presenti.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md](https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md)
- [https://github.com/amplify-education/python-hcl2](https://github.com/amplify-education/python-hcl2)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hcl` | [hello.hcl](hello.hcl) verificato |
| `.nomad` | [hello.nomad](variants/ext-nomad-2e6e6f6d6164/hello.nomad) creato, verifiche pendenti |
| `.tf` | [hello.tf](variants/ext-tf-2e7466/hello.tf) creato, verifiche pendenti |
| `.tfvars` | [hello.tfvars](variants/ext-tfvars-2e746676617273/hello.tfvars) creato, verifiche pendenti |
| `.tofu` | [hello.tofu](variants/ext-tofu-2e746f6675/hello.tofu) creato, verifiche pendenti |
| `.workflow` | [hello.workflow](variants/ext-workflow-2e776f726b666c6f77/hello.workflow) creato, verifiche pendenti |
