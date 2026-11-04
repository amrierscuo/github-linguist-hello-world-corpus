# #168 Dockerfile

Build and execute a container that prints Hello, World! with printf.

## Toolchain

Node.js v22.20.0; dockerfile-ast 0.7.1

## Commands and procedure

npm install; node check.cjs; docker build -t linguist-hello-dockerfile .; docker run --rm linguist-hello-dockerfile

## Expected result

Parser: FROM alpine: 3.22.2 and CMD exec-form correct; runtime predicted stdout Hello, World! more newline, exit 0.

## Status

syntax verified; behavioral verification pending.

Local parsing of the Dockerfile with community library and parsing JSON native CMD. The Daemon Docker is not active: no container has been built or executed. The base version is explicit; a future build will require access to the Alpine image. No publication planned.

Actual verification of 2026-10-08T12:00:44.301455+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

Remaining requirements:
- Docker Engine not running: named pipe dockerDesktopLinuxEngine absent; build/run pending.

## Primary sources and format reference

- [https://docs.docker.com/reference/dockerfile/](https://docs.docker.com/reference/dockerfile/)
- [https://github.com/rcjsuen/dockerfile-ast](https://github.com/rcjsuen/dockerfile-ast)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dockerfile` | [hello.dockerfile](variants/ext-dockerfile-2e646f636b657266696c65/hello.dockerfile) created; verification pending |
| `.containerfile` | [hello.containerfile](variants/ext-containerfile-2e636f6e7461696e657266696c65/hello.containerfile) created; verification pending |
