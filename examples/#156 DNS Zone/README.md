# #156 DNS Zone

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Validare una zona DNS e preservare un record TXT greeting con valore Hello, World!.

La zona contiene SOA, NS, A per il nameserver e il TXT del saluto. Usa il dominio riservato .example e l’indirizzo di documentazione 192.0.2.1. Il tool originale BIND controlla sintassi e integrità, senza avviare server DNS o modificare resolver del sistema.

## Toolchain e riproduzione

ISC BIND named-checkzone 9.18.39-0ubuntu0.24.04.7-Ubuntu

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
named-checkzone -D -o normalized.zone corpus.example hello.zone
```

## Risultato atteso e stato

Zona accettata con serial 2026100801, OK ed exit 0; dump canonico conserva greeting.corpus.example. TXT "Hello, World!".

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://bind9.readthedocs.io/en/latest/manpages.html#named-checkzone-zone-file-validation-tool
- https://www.isc.org/bind/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.zone` | [hello.zone](hello.zone) verificato |
| `.arpa` | [hello.arpa](variants/ext-arpa-2e61727061/hello.arpa) creato, verifiche pendenti |
