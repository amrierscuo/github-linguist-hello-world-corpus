# #208 Fennel

Voce canonica `Fennel`, tipo `programming`, language_id `239946126`.

Compilare un programma Fennel in Lua e concatenare/stampare il destinatario.

## Toolchain e riproduzione

Official Fennel compiler/interpreter CLI with Lua 5.4 — Fennel 1.6.0; Lua 5.4.6  Copyright (C) 1994-2023 Lua.org, PUC-Rio. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Compiler/CLI Fennel ufficiale 1.6.0 e Lua 5.4.6. fennel-1.6.0 è lo script compiler originale, posto in una directory strumenti esterna al corpus.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
lua5.4 fennel-1.6.0 --compile hello.fnl; lua5.4 fennel-1.6.0 hello.fnl
```

Risultato atteso: Compilazione riuscita; esecuzione exit 0 e saluto esatto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prima invocazione produce il vero Lua compilato; la seconda esegue lo stesso sorgente con il runtime autentico. I checksum di compiler e interprete sono nel log.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://fennel-lang.org/](https://fennel-lang.org/)
- [https://fennel-lang.org/downloads/fennel-1.6.0](https://fennel-lang.org/downloads/fennel-1.6.0)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fnl` | [hello.fnl](hello.fnl) verificato |
