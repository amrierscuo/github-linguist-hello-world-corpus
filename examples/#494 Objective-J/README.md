# #494 Objective-J

Voce canonica e ordine originali di reference/languages.yml.

Compilare e invocare un metodo Objective-J originale.

## Toolchain e riproduzione

objj-transpiler 1.0.0-10; objj-runtime 0.4.6; Node.js 22.20.0. Prova eseguita su Windows x64. Le versioni effettive sono nel log.

Dalla cartella dell'esempio, installare dipendenze isolate e verificare:

```text
npm --prefix .tools install --save-exact objj-transpiler@1.0.0-10 objj-runtime@0.4.6
node verify.cjs .tools hello.j
```

## Stato ed evidenza

Artefatto creato; sintassi verificata; semantica verificata.

Il compilatore originale produce JavaScript, valutato con le funzioni di classe e dispatch del runtime Objective-J originale. Il checker invoca main e controlla il messaggio emesso. Questa procedura evita soltanto il file loader Windows del runtime, mantenendo compilatore e dispatcher nativi.

Risultato atteso: Hello, World!.

Log reale: [verification/result.json](verification/result.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Fonti primarie

- [https://www.cappuccino.dev/learn/objective-j.html](https://www.cappuccino.dev/learn/objective-j.html)
- [https://github.com/mrcarlberg/objj-runtime](https://github.com/mrcarlberg/objj-runtime)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.j` | [hello.j](hello.j) sintassi e semantica verificate |
| `.sj` | [hello.sj](variants/sj-c6e9356b/hello.sj) sintassi e semantica verificate |
