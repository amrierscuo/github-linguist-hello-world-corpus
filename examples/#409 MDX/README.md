# #409 MDX

Fill in MDX with a JavaScript expression and make a HTML greeting title.

Canonical type `markup`, language_id `512838272`.

Suggested toolchain: Node.js 22, @mdx-js/mdx 3.1.1, React/ReactDOM 19.2.0.

From the example directory:

```sh
node verify.cjs
```

Expected result: HTML exactly <h1> Hello, World! </h1>; stdout greeting and LF.

Il runtime React esegue il componente generato dal compilatore MDX. Non viene avviato un browser o server web.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + @mdx-js/mdx 3.1.1 + React/ReactDOM 19.2.0. [Log](verification/result.json).

Sources:

- [MDX — evaluate API](https://mdxjs.com/packages/mdx/#evaluatefile-options)
- [MDX — sintassi](https://mdxjs.com/docs/what-is-mdx/)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund @mdx-js/mdx@3.1.1 react@19.2.0 react-dom@19.2.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mdx` | [hello.mdx](hello.mdx) verified |
