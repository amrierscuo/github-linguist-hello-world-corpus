# #740 V

Il sorgente originale compila con V e stampa `Hello, World!`.

Tipo canonico `programming`, language_id `603371597`.

## Toolchain e riproduzione

Prova eseguita con il compilatore ufficiale V 0.5.2 (commit `7647ce1`) e GCC 13.3.0 in Ubuntu 24.04 WSL2, architettura x86_64.

Dalla cartella dell'esempio, con una cartella di output già creata:

```sh
v -cc gcc -o build/hello hello.v
./build/hello
```

Il comando di compilazione termina con exit code 0. Il binario nativo restituisce esattamente `Hello, World!` seguito da newline e termina con exit code 0.

## Stato ed evidenza

Sintassi e semantica verificate. La sola presenza del file `.v` non determina questo stato: il compilatore V ha accettato i byte registrati e il binario è stato eseguito.

[Log nativo](verification/native.json) con comandi effettivi, timestamp UTC, versioni, stdout/stderr e SHA256 di sorgente, toolchain e prodotto compilato. I percorsi personali sono sostituiti da `<corpus>`, `<work>` e `<workspace>`; i byte del sorgente rimangono invariati.

## Fonti primarie

- [Documentazione V](https://docs.vlang.io/)
- [Release ufficiale V 0.5.2](https://github.com/vlang/v/releases/tag/0.5.2)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.v` | [hello.v](hello.v) sintassi e semantica verificate |
