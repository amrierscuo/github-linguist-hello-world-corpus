# #154 DIGITAL Command Language

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Eseguire una procedura OpenVMS DCL che concatena e scrive Hello, World!.

Il file .com è una procedura DIGITAL Command Language. Ogni riga di comando comincia con $, greeting è un simbolo stringa e WRITE usa SYS$OUTPUT. Lo status OpenVMS 1 indica successo; non è il codice POSIX di errore 1.

## Toolchain e riproduzione

VSI OpenVMS con DCL; versione effettiva da registrare

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
@HELLO.COM
```

## Risultato atteso e stato

SYS$OUTPUT contiene Hello, World! e newline; EXIT 1 è lo status di successo OpenVMS.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; parser/compilatore/runtime nativo non è stato eseguito per questa voce.

Impedimenti: OpenVMS/DCL non disponibile; nessun interprete nativo è stato eseguito.

## Fonti primarie

- https://docs.vmssoftware.com/vsi-openvms-dcl-dictionary-a-m/
- https://docs.vmssoftware.com/vsi-openvms-dcl-dictionary-n-z/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.com` | [hello.com](hello.com) creato, verifiche pendenti |
