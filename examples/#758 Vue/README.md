# #758 Vue

Compilare un Vue Single File Component ed eseguirne il rendering server-side.

Tipo canonico `markup`, language_id `391`.

Toolchain prevista: Node.js22.20.0 + Vue3.5.43 compiler-sfc/server-renderer and esbuild.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: SSR HTML esatto <p>Hello, World!</p>.

La semantica dichiarata è il rendering SSR originale; non certifica eventi o interazioni del browser.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Vue3 compiler-sfc/server-renderer + esbuild original compilers. [Log](verification/result.json). 

Fonti:

- [Vue SFC](https://vuejs.org/api/sfc-spec.html)
- [Vue SSR](https://vuejs.org/guide/scaling-up/ssr.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install vue @vue/compiler-sfc @vue/server-renderer esbuild
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vue` | [Hello.vue](Hello.vue) verificato |
