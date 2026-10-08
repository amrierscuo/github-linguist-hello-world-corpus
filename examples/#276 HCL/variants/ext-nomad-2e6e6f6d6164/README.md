# 0276 HCL — variante `.nomad`

Ruolo: Job HashiCorp Nomad batch con task raw_exec; verifica di parsing offline prima di qualunque scheduler.

Tipo variante: **adapted**. Modello di partenza: examples/#276 HCL/hello.hcl; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
nomad job validate hello.nomad (offline/istanza temporanea; nessuna esecuzione scheduler effettuata)
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
- [https://developer.hashicorp.com/nomad/docs/job-specification](https://developer.hashicorp.com/nomad/docs/job-specification)
