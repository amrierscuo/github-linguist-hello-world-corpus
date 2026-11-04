# #381 Less

Fill Less and make Hello, World! with a pseudo-element CSS.

## Toolchain

less 4.9.1; Node 22.20.0; Chrome 154.0.8037.98

## Commands and procedure

npm install; npx lessc hello.less build/hello.css; copiare hello.html in build e aprirlo con Chrome; controllare #result

## Expected result

content of:before is Hello, World!; color rgb( 18, 69, 120 ); pass=true.

## Status

syntax and behavior verified.

The file uses Less variables, interpolation and nesting. The original compiler generates CSS; Chromium loads the CSS and controls stile/computed content real. hello.html is the consumer/checker; CSS compiled and browser profile are only in work.

Actual verification of 2026-10-08T12:49:26.160251+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://lesscss.org/usage/](https://lesscss.org/usage/)
- [https://lesscss.org/features/](https://lesscss.org/features/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.less` | [hello.less](hello.less) verified |
