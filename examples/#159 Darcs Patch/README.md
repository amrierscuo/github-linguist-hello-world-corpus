# #159 Darcs Patch

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Applicare un bundle Darcs originale e ottenere greeting.txt contenente Hello, World!.

hello.dpatch è un vero patch bundle generato da darcs record/send per un originale greeting.txt. La verifica lo applica a un secondo repository locale e confronta i byte. send usa --output e un percorso locale: non sono inviate email o richieste a destinatari esterni. Il contesto vuoto esportato dal destinatario mantiene l’intestazione illustrativa CONTEXT senza percorsi locali. Il bundle è distinto da un diff unificato.

## Toolchain e riproduzione

Darcs 2.16.3 release, binario Windows ufficiale

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
Preparare due repository locali origin e receiver con darcs init.
Da receiver: darcs log --context > ../origin/receiver.context
Da origin: darcs add greeting.txt; darcs record --all --name "Add original corpus greeting" --author "Corpus Example <corpus@example.invalid>"
darcs send --all --no-edit-description --no-set-default --context receiver.context --output hello.dpatch ../receiver
```

```text
Nel repository locale destinatario vuoto: darcs apply --all hello.dpatch
```

## Risultato atteso e stato

Applicazione exit 0 e greeting.txt esattamente Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://darcs.net/Using/Commands
- https://darcs.net/Using/Send
- https://darcs.net/Binaries

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.darcspatch` | [hello.darcspatch](variants/ext-darcspatch-2e64617263737061746368/hello.darcspatch) creato, verifiche pendenti |
| `.dpatch` | [hello.dpatch](hello.dpatch) verificato |
