# #179 EQ

Define a EQ Greeting class with static value method that returns Hello, World!.

## Toolchain

EQ del progetto Jkop; toolchain/spec versione non reperita

## Commands and procedure

Integrate Greeting.eq into a Jkop EQ project and call Greeting.value () in its harness; compiler command to identify

## Expected result

Metodo value restituisce esattamente Hello, World!.

## Status

Syntax and behavioral verification pending.

Linguist: header Jkop/Job and Esther Technologies, public class and public static methods with return(...). The syntax resembles C#, but is not treated as C# and does not invent a console entrypoint. The fragment is original and the EQ toolchain remains to be identified before any verification flag.

Remaining requirements:
- Compilatore/runtime EQ of the Jkop project not identified; no syntactic verification or method call.

## Primary sources and format reference

- [https://github.com/github-linguist/linguist/blob/main/samples/EQ/String.eq](https://github.com/github-linguist/linguist/blob/main/samples/EQ/String.eq)
- [https://github.com/github-linguist/linguist/blob/main/samples/EQ/SEButtonEntity.eq](https://github.com/github-linguist/linguist/blob/main/samples/EQ/SEButtonEntity.eq)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.eq` | [Greeting.eq](Greeting.eq) created; verification pending |
