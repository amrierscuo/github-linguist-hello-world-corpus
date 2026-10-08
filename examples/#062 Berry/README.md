# #062 Berry

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Compilare ed eseguire una concatenazione di stringhe nella VM Berry.

La build dell’interprete originale omette soltanto la dipendenza opzionale readline per la console interattiva. Il parser e la VM di esecuzione file sono quelli del progetto upstream.

## Toolchain e riproduzione

Berry 1.1.0, sorgenti originali berry-lang/berry; GNU C su Ubuntu WSL

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
make CFLAGS="-Wall -Wextra -std=c99 -O2" LIBS="-lm -ldl"
```

```text
berry hello.be
```

## Risultato atteso e stato

stdout esatto: Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://github.com/berry-lang/berry
- https://berry.readthedocs.io/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.be` | [hello.be](hello.be) verificato |
