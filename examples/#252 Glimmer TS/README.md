# #252 Glimmer TS

Define a Glimmer TS component with greeting typed string and interpolation in the title.

## Toolchain

Node.js v22.20.0; content-tag 4.2.1, @glimmer/syntax 0.95.0, @babel/core 8.0.7, @babel/preset-typescript 8.0.7

## Commands and procedure

npm install; node check.cjs; integrare hello.gts in app Ember con Glint/TypeScript e renderizzarlo

## Expected result

Parser accepts TypeScript/template-tag; Glint type check; runtime makes the title Hello, World!.

## Status

syntax verified; behavioral verification pending.

SWC/content-tag and Babel TypeScript really analyze the file; Glimmer solves the AST structure {{greeting}}. Babel removes the annotation but is not a complete type checker. Type check Glint and DOM rendering Ember remain pending.

Actual verification of 2026-10-08T12:17:25.882443+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

Remaining requirements:
- Ember application/runtime DOM rendering not yet performed.
- Glint/TypeScript full type check pending.

## Primary sources

- [https://github.com/ember-cli/ember-template-imports](https://github.com/ember-cli/ember-template-imports)
- [https://github.com/embroider-build/content-tag](https://github.com/embroider-build/content-tag)
- [https://typed-ember.gitbook.io/glint](https://typed-ember.gitbook.io/glint)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gts` | [hello.gts](hello.gts) syntax verified |
