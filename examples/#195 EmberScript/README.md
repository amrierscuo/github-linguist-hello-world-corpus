# #195 EmberScript

Compilare un sorgente EmberScript con il compilatore originale ed eseguire il JavaScript per stampare Hello, World!.

Tipo canonico `programming`, language_id `103`.

Toolchain prevista: Node.js 22 ed ember-script 0.0.14.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: stdout `Hello, World!\n`, uscita 0.

Il saluto usa una chiamata alla console che non dipende da classi Ember. Resta un sorgente EmberScript; viene compilato dal suo compilatore, non da CoffeeScript puro.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + ember-script 0.0.14. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [EmberScript — progetto originale](https://github.com/ghempton/ember-script)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund ember-script@0.0.14
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.em` | [hello.em](hello.em) verificato |
| `.emberscript` | [hello.emberscript](variants/ext-emberscript-2e656d626572736372697074/hello.emberscript) creato, verifiche pendenti |
