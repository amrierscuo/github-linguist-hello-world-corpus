# #034 Apex

Costruire Hello, World!, controllarla con System.assertEquals e registrarla con System.debug in un blocco Apex anonimo.

## File

- `hello.apex`
- `check.cjs`
- `package.json`

## Toolchain e verifica

Node.js v22.20.0; @apexdevtools/apex-parser 5.2.0 (parser comunitario). Semantica: Salesforce CLI e org di sviluppo autenticata.

Eseguire i comandi nella cartella dell'esempio. `package.json` fissa il parser
comunitario alla versione 5.2.0. `check.cjs` raccoglie errori del lexer e del
parser e usa l'ingresso `anonymousUnit` appropriato per un blocco anonimo.

```powershell
npm install
node check.cjs
```

Per completare la semantica usare una org di sviluppo autenticata, sostituendo
`ALIAS` con il proprio alias; registrare anche `sf --version` e il log restituito.

```powershell
sf apex run --file hello.apex --target-org ALIAS
```

Il risultato del parser locale attesta la grammatica accettata dalla toolchain
comunitaria. Il controllo dei tipi e `System.assertEquals` saranno eseguiti dalla
piattaforma Salesforce solo nella prova ancora pendente.

## Risultato atteso

Controllo locale: zero errori lexer/parser, exit 0. Su Salesforce: assertEquals passa e log USER_DEBUG contiene Hello, World!.

## Stato della prova

Sintassi verificata. Semantica in attesa.

Sintassi verificata dal parser comunitario ANTLR; questo controllo non esegue la compilazione Salesforce né l'assert Apex.

Prova effettiva Windows x64 del 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
Il log include hash SHA-256 della sorgente, versioni osservate, comandi, codici di uscita, stdout e stderr.

Requisiti residui:
- Esecuzione e controllo dei tipi Salesforce non eseguiti: occorrono una org di sviluppo autenticata e Salesforce CLI.

## Fonti primarie

- [https://github.com/apex-dev-tools/apex-parser](https://github.com/apex-dev-tools/apex-parser)
- [https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html](https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cls` | [CorpusGreeting.cls](variants/ext-cls-2e636c73/CorpusGreeting.cls) creato, verifiche pendenti |
| `.apex` | [hello.apex](hello.apex) sintassi verificata |
| `.trigger` | [hello.trigger](variants/ext-trigger-2e74726967676572/hello.trigger) creato, verifiche pendenti |
