# #409 MDX

Compilare MDX con un’espressione JavaScript e renderizzare un titolo HTML di saluto.

Tipo canonico `markup`, language_id `512838272`.

Toolchain prevista: Node.js 22, @mdx-js/mdx 3.1.1, React/ReactDOM 19.2.0.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: HTML esattamente <h1>Hello, World!</h1>; stdout saluto e LF.

Il runtime React esegue il componente generato dal compilatore MDX. Non viene avviato un browser o server web.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + @mdx-js/mdx 3.1.1 + React/ReactDOM 19.2.0. [Log](verification/result.json). 

Fonti:

- [MDX — evaluate API](https://mdxjs.com/packages/mdx/#evaluatefile-options)
- [MDX — sintassi](https://mdxjs.com/docs/what-is-mdx/)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund @mdx-js/mdx@3.1.1 react@19.2.0 react-dom@19.2.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mdx` | [hello.mdx](hello.mdx) verificato |
