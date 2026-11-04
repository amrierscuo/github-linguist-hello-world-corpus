# #310 ImageJ Macro

Run an original macro ImageJ in batch and print greetings.

## Toolchain

ImageJ 1.54g; Microsoft OpenJDK 21.0.12.1

## Commands and procedure

java -Djava.awt.headless=true -jar ij.jar -batch hello.ijm

## Expected result

Runtime exit 0; stdout Hello, World! plus newline.

## Status

syntax and behavior verified.

The macro uses print, without GUI operations or images. ImageJVersion.java consults the real runtime to record ij.IJ.getVersion (); it does not implement the macro interpreter.

Actual verification of 2026-10-08T12:29:58.567762+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://imagej.net/ij/plugins/command-line-macros.html](https://imagej.net/ij/plugins/command-line-macros.html)
- [https://imagej.net/ij/developer/macro/functions.html](https://imagej.net/ij/developer/macro/functions.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ijm` | [hello.ijm](hello.ijm) verified |
