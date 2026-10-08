# #446 MoonBit

Voce canonica `MoonBit`, tipo `programming`, language_id `181453007`.

Compilare un progetto MoonBit originale e stampare il saluto nel target JavaScript.

## Toolchain e riproduzione

Official MoonBit compiler/build tool and core standard library — moon 0.1.20260920 (914d7da 2026-09-20); ; Feature flags enabled: rr_moon_mod,rr_moon_pkg. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

MoonBit ufficiale e core standard library: distribuzione Windows portabile, MOON_HOME locale. La preparazione del core usa moon bundle --target js --all dalla directory lib/core.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
moon run --target js cmd/main
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Compiler e build tool autentici accettano il progetto e il target JS produce il testo esatto. La vecchia configurazione JSON è ancora accettata con avviso di deprecazione.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.moonbitlang.com/download](https://www.moonbitlang.com/download)
- [https://docs.moonbitlang.com/en/latest/tutorial/index.html](https://docs.moonbitlang.com/en/latest/tutorial/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mbt` | [main.mbt](cmd/main/main.mbt) verificato |
