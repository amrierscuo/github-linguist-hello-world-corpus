# #251 Glimmer JS

Define a template-only component Glimmer JS with Hello, World! title.

## Toolchain

Node.js v22.20.0; content-tag 4.2.1, @glimmer/syntax 0.95.0, @babel/core 8.0.7, @babel/preset-typescript 8.0.7

## Commands and procedure

npm install; node check.cjs; integrate hello.gjs as a component in a compatible Ember app and make it

## Expected result

Parser accetta template-tag e JavaScript generato; runtime Ember rende <h1>Hello, World!</h1>.

## Status

syntax verified; behavioral verification pending.

content-tag uses the Rust/SWC preprocessor in WASM; Glimmer analyzes the template and Babel the host code generated. The title in the AST template is verified. This compilazione/parsing test does not attest to the rendering of the Ember component, which remains pending.

Actual verification of 2026-10-08T12:17:25.190660+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

Remaining requirements:
- Ember application/runtime DOM rendering not yet performed.

## Primary sources

- [https://github.com/ember-cli/ember-template-imports](https://github.com/ember-cli/ember-template-imports)
- [https://github.com/embroider-build/content-tag](https://github.com/embroider-build/content-tag)
- [https://github.com/glimmerjs/glimmer-vm](https://github.com/glimmerjs/glimmer-vm)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gjs` | [hello.gjs](hello.gjs) syntax verified |
