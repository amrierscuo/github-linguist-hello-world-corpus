# #494 Objective-J .sj

Archivio Static-J autentico generato dal sorgente principale hello.j. Non è una rinomina del sorgente Objective-J: contiene il codice compilato con intestazione @STATIC e record testuale serializzati dal runtime originale.

## Toolchain e riproduzione

Node.js 22.20.0, objj-transpiler 1.0.0-10 e objj-runtime 0.4.6.

Dalla cartella principale dell'esempio:

```text
npm --prefix .tools install --save-exact objj-transpiler@1.0.0-10 objj-runtime@0.4.6
node make-sj.cjs .tools hello.j variants/sj-c6e9356b/hello.sj
node verify.cjs .tools variants/sj-c6e9356b/hello.sj
```

Il compilatore originale produce JavaScript e Executable.toMarkedString genera l'archivio. FileExecutable del runtime originale analizza i byte .sj; il codice decodificato viene eseguito con le funzioni originali di classe e dispatch. Il checker invoca main e verifica il messaggio Hello, World!. Node fornisce soltanto il caricamento locale dei byte per evitare il file loader Windows non funzionante.

Artefatto creato; sintassi verificata; semantica verificata.

Log reale: [verification/native.json](verification/native.json), con comandi, versioni del toolchain usato, exit code, stdout/stderr e SHA-256.

## Fonti primarie

- https://github.com/mrcarlberg/objj-runtime
- https://github.com/cappuccino/cappuccino
- https://www.cappuccino.dev/learn/objective-j.html
