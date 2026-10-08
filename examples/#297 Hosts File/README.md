# #297 Hosts File

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Analizzare un Hosts File illustrativo che associa hello-world.example.invalid a 192.0.2.1.

Un hostname non contiene spazi o punteggiatura del saluto: l’equivalente appropriato è il nome hello-world. Il parser originale Hosts legge soltanto il percorso esplicito della fixture; il file del sistema operativo non viene scritto né usato come resolver.

## Toolchain e riproduzione

python-hosts1.1.3, CPython3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Una voce IPv4 con indirizzo192.0.2.1 e nome hello-world.example.invalid; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://man7.org/linux/man-pages/man5/hosts.5.html
- https://github.com/jonhadfield/python-hosts
- https://www.rfc-editor.org/rfc/rfc6761.html
