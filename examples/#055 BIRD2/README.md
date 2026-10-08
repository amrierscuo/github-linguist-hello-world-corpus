# #055 BIRD2

Voce canonica: `BIRD2`, tipo `data`, language_id `584191811`.

Caricare una configurazione BIRD2 con costante GREETING = Hello, World! e una route blackhole nella tabella interna; leggere il saluto con il client BIRD.

## Toolchain e riproduzione

BIRD 2.14, pacchetto Ubuntu estratto localmente.

BIRD 2.14. Usare un socket Unix e un PID esclusivi su filesystem Linux. Avviare il daemon in una sessione separata e terminare sempre con birdc down.

Comandi dalla directory dell’esempio; `<output>` indica una directory temporanea esterna al corpus.

Terminale 1, dalla cartella dell'esempio:

```sh
bird -p -c bird.conf
bird -f -c bird.conf -s /tmp/corpus-bird.sock -P /tmp/corpus-bird.pid
```

Terminale 2, mentre il daemon del primo terminale è attivo:

```sh
birdc -s /tmp/corpus-bird.sock eval GREETING
birdc -s /tmp/corpus-bird.sock down
```

Risultato atteso: Parser exit 0; il client BIRD restituisce la riga Hello, World!; daemon isolato terminato con exit 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser BIRD 2.14 accetta la configurazione. Un daemon con socket e PID isolati valuta GREETING tramite birdc, restituendo Hello, World!. La configurazione usa solo static e non contiene protocolli kernel/device, quindi non esporta route al sistema. Shutdown del processo verificato.

Prova reale: [finish.json](verification/finish.json), con UTC, comandi, versioni, exit code, stdout/stderr e SHA-256 dei sorgenti. Le sostituzioni dei percorsi sono documentate nel log. I prodotti di compilazione e le dipendenze rimangono nelle directory di lavoro.

## Fonti primarie

- https://bird.nic.cz/doc/bird-2.14.html
- https://bird.network.cz/doc/bird-3.html
