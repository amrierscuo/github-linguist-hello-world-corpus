# #142 Csound Document

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Eseguire un documento Csound completo che include opzioni, orchestra e score.

hello.csd è il formato unificato con CsOptions, CsInstruments e CsScore. Il runtime compila il documento e attiva lo strumento. Le opzioni -n -d -m0 non richiedono audio o dispositivi; il messaggio Csound è registrato su stderr. Il plugin directory warning riguarda plugin opzionali.

## Toolchain e riproduzione

Csound 6.18, pacchetto Ubuntu 6.18.1+dfsg-1ubuntu4 x86_64

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
csound hello.csd
```

## Risultato atteso e stato

Messaggio Hello, World! seguito da newline; 0 errors in performance e exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://csound.com/docs/manual/CommandUnifile.html
- https://csound.com/docs/manual/prints.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.csd` | [hello.csd](hello.csd) verificato |
