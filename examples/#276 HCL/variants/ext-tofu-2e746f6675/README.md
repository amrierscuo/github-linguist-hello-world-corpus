# 0276 HCL — variante `.tofu`

Ruolo: Configurazione OpenTofu HCL con locals/output senza provider.

Tipo variante: **adapted**. Modello di partenza: examples/#276 HCL/hello.hcl; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
OpenTofu nel progetto temporaneo: collocare come main.tofu; tofu init -backend=false; tofu apply -auto-approve; tofu output -raw message
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md](https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md)
- [https://github.com/amplify-education/python-hcl2](https://github.com/amplify-education/python-hcl2)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://opentofu.org/docs/language/](https://opentofu.org/docs/language/)
