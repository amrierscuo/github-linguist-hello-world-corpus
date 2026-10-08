# #141 Csound

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Eseguire un’orchestra Csound che stampa Hello, World! all’inizializzazione di instr 1.

hello.orc contiene il programma orchestra; schedule.sco attiva lo strumento. Il saluto proviene dall’opcode prints built-in. -n disabilita output audio; nessun dispositivo audio o file audio è usato. L’avviso sulla directory dei plugin opzionali assente è registrato e non impedisce questa esecuzione.

## Toolchain e riproduzione

Csound 6.18, pacchetto Ubuntu 6.18.1+dfsg-1ubuntu4 x86_64

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
csound -n -d -m0 hello.orc schedule.sco
```

## Risultato atteso e stato

Messaggio Hello, World! seguito da newline; 0 errors in performance e exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://csound.com/docs/manual/prints.html
- https://csound.com/docs/manual/CommandFlags.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.orc` | [hello.orc](hello.orc), [consumer.orc](variants/ext-udo-2e75646f/consumer.orc) creato, verifiche pendenti |
| `.udo` | [hello.udo](variants/ext-udo-2e75646f/hello.udo) creato, verifiche pendenti |
