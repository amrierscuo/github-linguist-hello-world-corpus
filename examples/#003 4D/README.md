# #003 4D

`HelloWorld.4dm` is the source of a project method 4D. The method recalls
`ALERT` and display `Hello, World!` in a window with OK button.

## Toolchain and commands

We need the **4D** application in development mode. Create an empty project,
create the `HelloWorld` project method and insert the file content.
The only `.4dm` is a source unit: this folder does not contain a project
4D complete or a binary database.

Comando reale di controllo nell'IDE: `Design > Compiler... > Check Syntax`.
Optional compilation, if licensed:
`Design > Compiler... > Compile`. For behavior verification, run the method
`HelloWorld` via the Explorer or the method execution command.

Expected result: no error from syntax control and a window with
exact text `Hello, World!`. To integrate the disk file into a project already
existing, the location of the methods is `Project/Sources/Methods/`.

## Status and limitations

Artifact created; syntax and behavior **non ancora verificate**. The application
4D is not available in this session. Filling instructions depend
from the host project and, for native compilation, the license.

## Official sources

- [4D, comando `ALERT`](https://developer.4d.com/docs/commands/alert).
- [4D, architettura del progetto e metodi `.4dm`](https://developer.4d.com/docs/Project/architecture).
- [4D, compilazione e `Check Syntax`](https://developer.4d.com/docs/Project/compiler).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.4dm` | [HelloWorld.4dm](HelloWorld.4dm) created; verification pending |
