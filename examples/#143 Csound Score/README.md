# #143 Csound Score

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Leggere una stringa p4 da uno score Csound e stamparla mediante l’orchestra di supporto.

hello.sco è uno score autentico: i-statement con strumento, tempo, durata e parametro stringa. reader.orc è una fixture che legge p4 tramite strget. Il saluto appartiene allo score, non è sostituito da una stampa costante nella fixture. Il plugin directory warning opzionale è registrato.

## Toolchain e riproduzione

Csound 6.18, pacchetto Ubuntu 6.18.1+dfsg-1ubuntu4 x86_64

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
csound -n -d -m0 reader.orc hello.sco
```

## Risultato atteso e stato

Il parametro p4 del primo evento è Hello, World! e il runtime stampa quel valore; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://csound.com/docs/manual/ScoreIStatement.html
- https://csound.com/docs/manual/strget.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sco` | [hello.sco](hello.sco) verificato |
