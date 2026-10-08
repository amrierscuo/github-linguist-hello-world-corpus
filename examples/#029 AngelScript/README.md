# #029 AngelScript

`hello.as` definisce `void main()` e chiama `print()` registrata dall'host del runner ufficiale `asrun`. `print` è una funzione dell'host dimostrativo, non una funzione intrinseca di ogni integrazione AngelScript.

Prerequisito: runner del campione `/sdk/samples/asrun/` dell'SDK AngelScript 2.38.0, compilato insieme al motore e agli add-on richiesti con un compilatore C++. Il runner Linux già compilato localmente è stato eseguito tramite Ubuntu WSL; la sua versione e il suo hash sono registrati nel log. Il binario non è incluso nel corpus.

```sh
asrun hello.as
```

Output atteso esatto:

```text
Hello, World!
```

La prova eseguita include compilazione in bytecode del sorgente da parte del motore e chiamata di `main()` nella VM. Invocare `asrun` senza file stampa versione e uso con exit 255: quel codice appartiene al comando informativo, mentre l'esecuzione dell'esempio termina con exit 0.

Toolchain: **AngelScript SDK 2.38.0; runner ufficiale asrun compilato con GNU C++ su Ubuntu WSL x86_64**.

Stato: **Sintassi e semantica verificate.**

Evidenza: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). Il log conserva exit code, stdout e stderr; i percorsi della macchina sono normalizzati.

Fonti primarie:

- [Documentazione / sorgente ufficiale 1](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_samples_asrun.html)
- [Documentazione / sorgente ufficiale 2](https://github.com/anjo76/angelscript/releases/tag/v2.38.0)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.as` | [hello.as](hello.as) verificato |
| `.angelscript` | [hello.angelscript](variants/ext-angelscript-2e616e67656c736372697074/hello.angelscript) creato, verifiche pendenti |
