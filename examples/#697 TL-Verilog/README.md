# #697 TL-Verilog

Voce canonica `TL-Verilog`, tipo `programming`, language_id `118656070`.

Tradurre un segnale TL-Verilog originale che porta i 13 byte ASCII del saluto a un output SV.

## Toolchain e riproduzione

Required genuine sandpiper-saas compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede translator TL-Verilog SandPiper/SVGen compatibile con TL-X1d e simulatore SV.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
sandpiper-saas -i hello.tlv -o build/hello.sv; iverilog -g2012 -o build/hello.vvp build/hello.sv; vvp build/hello.vvp
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il blocco TLV definisce il segnale e lo lega a un wire SV; il saluto eÌâ‚¬ dati hexadecimal, quindi una display del risultato rende il testo. Translator autentico non configurato; flag pending.

Requisiti residui:

- Required sandpiper-saas toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/TL-X-org/tlv-comp](https://github.com/TL-X-org/tlv-comp)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tlv` | [hello.tlv](hello.tlv) creato, verifiche pendenti |
