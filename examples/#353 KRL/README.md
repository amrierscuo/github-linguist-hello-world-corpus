# #353 KRL

Voce canonica `KRL`, tipo `programming`, language_id `186`.

Definire una regola Kinetic Rule Language che reagisce a corpus:hello e invia una direttiva greeting con il saluto.

## Toolchain e riproduzione

Authoritative Picolab KRL parser — krl-parser 1.5.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

krl-parser originale Picolab 1.5.0 su Node.js 22.20.0. La baseline Linguist identifica qui Kinetic Rule Language; la grammatica del package Picolab è autoritativa.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools krl-parser@1.5.0; node verify.cjs .tools build; per la semantica installare il ruleset in un Pico Engine locale e inviare l’evento corpus:hello
```

Risultato atteso: Parsing riuscito; runtime futuro restituisce direttiva greeting con message=Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Il parser originale accetta il ruleset e salva l’AST in build. Sintassi verificata; semantica pendente perché l’evento non viene eseguito nel Pico Engine. La direttiva contiene un valore effettivo, non solo metadata o commenti.

Requisiti residui:

- KRL grammar accepted by authoritative parser; event execution in a Pico Engine runtime is not performed.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://picolabs.atlassian.net/wiki/spaces/docs/pages/223117313/Grammar](https://picolabs.atlassian.net/wiki/spaces/docs/pages/223117313/Grammar)
- [https://picolabs.atlassian.net/wiki/spaces/docs/pages/1189832](https://picolabs.atlassian.net/wiki/spaces/docs/pages/1189832)
- [https://github.com/Picolab/pico-engine/tree/master/packages/krl-parser](https://github.com/Picolab/pico-engine/tree/master/packages/krl-parser)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.krl` | [hello.krl](hello.krl) sintassi verificata |
