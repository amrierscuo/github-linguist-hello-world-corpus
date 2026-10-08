# #797 YANG

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Validare un modello YANG1.1 e leggere il default Hello, World!.

Pyang controlla grammatica e vincoli del modello/default e il driver legge il leaf validato. L’obiettivo è il valore predefinito del modello; nessun dispositivo/NETCONF viene configurato.

## Toolchain e riproduzione

Pyang2.7.1 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Modello valido, leaf greeting di tipo string con default Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.rfc-editor.org/rfc/rfc7950.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.yang` | [corpus-greeting.yang](corpus-greeting.yang) verificato |
