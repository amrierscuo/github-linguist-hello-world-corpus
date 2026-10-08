# #055 BIRD2

Voce canonica: `BIRD2`, tipo `data`, `language_id: 584191811`.

Caricare una configurazione BIRD2 con costante GREETING = Hello, World! e una route blackhole nella tabella interna; leggere il saluto con il client BIRD.

## Toolchain e riproduzione

BIRD 2 Ubuntu binary package extracted locally — BIRD version 2.14. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Richiede BIRD 2.14. La prova disponibile esegue soltanto bird -p sul file indicato; non avvia un daemon e non modifica route del sistema. Per l’animazione usare un daemon dedicato con socket e PID isolati.

Comando/procedura dalla directory dell’esempio:

```text
bird -p -c bird.conf; BIRD daemon isolato: birdc -s <socket> eval GREETING
```

Risultato atteso: Parser exit 0; valutazione runtime attesa della costante GREETING uguale a Hello, World! (pending).

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

La configurazione usa il protocollo static, senza protocollo kernel e senza esportazioni verso il sistema. Il parser ufficiale l’ha accettata. La valutazione della stringa in una sessione BIRD non è stata ottenuta: semantica pending.

Requisiti residui:

- BIRD parser accepted the configuration; daemon/client runtime evaluation of GREETING remains pending.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://bird.nic.cz/doc/bird-2.14.html](https://bird.nic.cz/doc/bird-2.14.html)
- [https://bird.network.cz/doc/bird-3.html](https://bird.network.cz/doc/bird-3.html)
