# #704 TSX

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in TSX and make a React component with Hello, World!.

The typechecker TSX compiles the type component; React server maker evaluates the audience prop and produces static markup.

## Toolchain and reproduction

TypeScript, React and react-dom original; versions and lock SHA in the log

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
tsc --jsx react-jsx --module commonjs --target es2020 --skipLibCheck --outDir build hello.tsx; node render.cjs
```

## Expected result and status

<p>Hello, World!</p> su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.typescriptlang.org/docs/handbook/jsx.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tsx` | [hello.tsx](hello.tsx) verified |
