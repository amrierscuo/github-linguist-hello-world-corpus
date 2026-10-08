# #136 Cooklang

Voce canonica: `Cooklang`, tipo `markup`, `language_id: 788037493`.

Rappresentare il saluto come titolo e istruzione di una ricetta Cooklang e verificare gli oggetti estratti: acqua, recipienti e timer.

## Toolchain e riproduzione

Official CookCLI Cooklang parser — cookcli 0.37.0 - in food we trust. Ambiente della prova: **Windows x64**.

CookCLI ufficiale 0.37.0 portable Windows x64. La ricetta usa YAML frontmatter, ingredienti @, cookware # e timer ~ secondo le estensioni supportate da questa versione.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
cook --version; cook recipe hello.cook --format json
```

Risultato atteso: JSON valido: title Hello, World!, servings 1, water 250 ml, cookware kettle/cup, timer 1 minutes; parsing exit 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser autentico produce il modello JSON, e la prova confronta i valori strutturati sopra indicati. È una verifica dei dati della ricetta, non una esecuzione o un risultato fisico di cucina. Non serve la funzione import con AI né una chiave API.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://cooklang.org/docs/spec/](https://cooklang.org/docs/spec/)
- [https://cooklang.org/cli/commands/recipe/](https://cooklang.org/cli/commands/recipe/)
- [https://github.com/cooklang/cookcli/releases/tag/v0.37.0](https://github.com/cooklang/cookcli/releases/tag/v0.37.0)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cook` | [hello.cook](hello.cook) verificato |
