# #713 Teal

Voce canonica `Teal`, tipo `programming`, language_id `719038619`.

Controllare i tipi Teal, generare Lua ed eseguire Hello, World!.

## Toolchain e riproduzione

Teal originale dal repository teal-language/tl e Lua5.4.6.

Occorrono il compilatore originale Teal, Lua 5.4.6 e i moduli LuaFileSystem/compat53 della prova. Eseguire check/gen e Lua in una copia temporanea per tenere hello.lua fuori dal corpus.

```text
tl check hello.tl; tl gen hello.tl; lua hello.lua
```

Risultato atteso: Typecheck e generazione exit 0; runtime exit 0, stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Un commento Teal descrive il tipo string esplicito del destinatario. Il compilatore originale ricontrolla i tipi, genera Lua, e Lua5.4 esegue il risultato con saluto esatto. Commento e dichiarazione typed local distinguono il file .tl da Type Language.

Prova corrente: [recognition.json](verification/recognition.json), con UTC, comandi nativi, exit code, stdout/stderr, toolchain e SHA-256 dei sorgenti modificati e dei driver. Le prove precedenti restano come storico. L’identificazione prevista da Linguist è distinta dall’esito effettivo delle statistiche GitHub; questo lotto non applica override di linguaggio.

## Fonti primarie

- https://github.com/teal-language/tl
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.tl` | [hello.tl](hello.tl) sintassi e semantica verificate |
