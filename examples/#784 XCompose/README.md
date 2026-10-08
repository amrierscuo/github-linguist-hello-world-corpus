# #784 XCompose

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare XCompose e produrre Hello, World! dalla sequenza Multi_key,h,w.

Il parser XCompose nativo legge una fixture via buffer e la macchina a stati riceve tre keysyms. Nessun server X, tastiera fisica o file di configurazione del sistema viene modificato.

## Toolchain e riproduzione

Libxkbcommon originale1.6.0, Python ctypes

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python3 verify.py /path/to/libxkbcommon.so.0
```

## Risultato atteso e stato

Stato COMPOSED e stringa UTF8 Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://xkbcommon.org/doc/current/group__compose.html
