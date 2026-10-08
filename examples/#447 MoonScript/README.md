# #447 MoonScript

Voce canonica `MoonScript`, tipo `programming`, language_id `238`.

Compilare un sorgente MoonScript con interpolazione e poi eseguire il Lua generato.

## Toolchain e riproduzione

Official MoonScript compiler with LPeg and genuine Lua — MoonScript 0.5.0; Lua 5.4.6  Copyright (C) 1994-2023 Lua.org, PUC-Rio. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

MoonScript 0.5.0 originale, LPeg e Lua 5.4.6. I due valori env contenenti ; vanno passati come argomenti singoli/quotati nella shell. Creare build prima della verifica.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
LUA_PATH=/path/to/moonscript/?.lua;/path/to/moonscript/?/init.lua;; LUA_CPATH=/path/to/lpeg/?.so;; lua5.4 verify.lua hello.moon build/hello.lua
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La libreria moonscript.base.to_lua autentica genera codice; il runtime Lua lo carica ed esegue. Nessun parser sostitutivo.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://moonscript.org/](https://moonscript.org/)
- [https://github.com/leafo/moonscript](https://github.com/leafo/moonscript)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.moon` | [hello.moon](hello.moon) verificato |
