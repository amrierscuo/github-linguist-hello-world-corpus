# #281 HTML+ECR

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Renderizzare un template HTML+ECR con pubblico World e produrre il paragrafo Hello, World!.

ECR.render incorpora il template nel programma Crystal durante la compilazione. audience è un valore del contesto Crystal interpolato nell’HTML. La verifica compila ed esegue il renderer originale; cache, oggetti e binario restano in work.

## Toolchain e riproduzione

Crystal 1.11.2, LLVM17.0.6, ECR stdlib; GNU linker e PCRE8.39 isolata

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
crystal build render.cr -o render
```

```text
./render
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://crystal-lang.org/api/1.11.2/ECR.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ecr` | [hello.ecr](hello.ecr) verificato |
