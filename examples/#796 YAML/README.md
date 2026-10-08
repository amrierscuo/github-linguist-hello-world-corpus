# #796 YAML

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare YAML e leggere la stringa Hello, World!.

Il safe loader interpreta un mapping YAML originale; il driver controlla il valore scalare.

## Toolchain e riproduzione

PyYAML6.0.3 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Mapping con greeting = Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://pyyaml.org/wiki/PyYAMLDocumentation

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.yml` | [hello.yml](hello.yml) verificato |
| `.mir` | [hello.mir](variants/mir-c4950490/hello.mir) verificato |
| `.reek` | [hello.reek](variants/reek-d43e4b53/hello.reek) creato, verifiche pendenti |
| `.rviz` | [hello.rviz](variants/rviz-2327f1f4/hello.rviz) creato, verifiche pendenti |
| `.sublime-syntax` | [hello.sublime-syntax](variants/sublime-syntax-35002c21/hello.sublime-syntax) creato, verifiche pendenti |
| `.syntax` | [hello.syntax](variants/syntax-0ed79f06/hello.syntax) creato, verifiche pendenti |
| `.yaml` | [hello.yaml](variants/yaml-fa1b82e8/hello.yaml) creato, verifiche pendenti |
| `.yaml-tmlanguage` | [hello.yaml-tmlanguage](variants/yaml-tmlanguage-f2fa8d15/hello.yaml-tmlanguage) creato, verifiche pendenti |
| `.yaml.sed` | [hello.yaml.sed](variants/yaml-sed-463fad60/hello.yaml.sed) creato, verifiche pendenti |
| `.yml.mysql` | [hello.yml.mysql](variants/yml-mysql-d412fc04/hello.yml.mysql) creato, verifiche pendenti |
