# #631 SELinux Policy

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare un modulo SELinux che dichiara il tipo hello_world_t.

hello_world_t è l’equivalente identificatore del saluto per una policy. Il compilatore controlla modulo, tipi e regola allow; la policy non viene caricata nel sistema.

## Toolchain e riproduzione

Checkmodule3.5 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
checkmodule -M -m -o corpus_greeting.mod hello.te
```

## Risultato atteso e stato

Compilazione del modulo termina con exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Comportamento della policy non verificato su un sistema SELinux; semantica operativa pendente.

## Fonti primarie

- https://github.com/SELinuxProject/selinux-notebook/blob/main/src/modular_policy_statements.md?plain=1

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.te` | [hello.te](hello.te) sintassi verificata |
