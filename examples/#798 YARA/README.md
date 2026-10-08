# #798 YARA

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare YARA e riconoscere la fixture Hello, World!.

Il motore nativo compila la regola e riconosce il saluto; il controllo negativo Hello, Moon! non deve corrispondere.

## Toolchain e riproduzione

YARA/yara-python4.5.4 originali

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Una corrispondenza CorpusGreeting per Hello, World!, nessuna per Hello, Moon!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://yara.readthedocs.io/en/stable/writingrules.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.yar` | [hello.yar](hello.yar) verificato |
| `.yara` | [hello.yara](variants/yara-cc22c747/hello.yara) creato, verifiche pendenti |
