# #068 BitBake

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Eseguire una ricetta BitBake originale con un task Python do_build che emette Hello, World!.

La ricetta .bb, la configurazione del layer, la classe base e bblayers.conf costituiscono un progetto minimo indipendente da una distribuzione Yocto. Il task non produce pacchetti o immagini. I comandi richiedono bitbake nel PATH e locale en_US.UTF-8.

## Toolchain e riproduzione

BitBake upstream branch 2.10; Python 3.12.3 su Ubuntu WSL

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
Da build/: BBPATH="$PWD" bitbake -p
```

```text
Da build/: BBPATH="$PWD" bitbake hello
```

## Risultato atteso e stato

Metadata accettati e task do_build riuscito con messaggio Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

Impedimenti: Il BitBake reale richiede en_US.UTF-8, non presente nel WSL; si arresta all’avvio prima del parser. LC_ALL=C.UTF-8 non soddisfa questo requisito; nessun server è stato avviato.

## Fonti primarie

- https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html
- https://github.com/openembedded/bitbake/tree/2.10

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bb` | [hello_1.0.bb](meta-hello/hello_1.0.bb), [hello_1.0.bb](variants/ext-bbappend-2e6262617070656e64/hello_1.0.bb), [hello_1.0.bb](variants/ext-inc-2e696e63/hello_1.0.bb) creato, verifiche pendenti |
| `.bbappend` | [hello_1.0.bbappend](variants/ext-bbappend-2e6262617070656e64/hello_1.0.bbappend) creato, verifiche pendenti |
| `.bbclass` | [base.bbclass](meta-hello/classes/base.bbclass) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) creato, verifiche pendenti |
