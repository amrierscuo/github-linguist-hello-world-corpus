# #649 Scala

Fill Scale and run main on the JVM.

## Toolchain

Scala compiler version 2.13.16 -- Copyright 2002-2025, LAMP/EPFL and Lightbend, Inc. dba Akka

## Procedure

scalac Hello.scala -d build; java -cp build:<scala-library.jar> Hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:23:07.902520+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://docs.scala-lang.org/scala3/book/taste-hello-world.html](https://docs.scala-lang.org/scala3/book/taste-hello-world.html)
- [https://github.com/scala/scala/releases/tag/v2.13.16](https://github.com/scala/scala/releases/tag/v2.13.16)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.scala` | [Hello.scala](Hello.scala) verified |
| `.kojo` | [hello.kojo](variants/kojo-eb37572d/hello.kojo) created; verification pending |
| `.sbt` | [hello.sbt](variants/sbt-8cfa3e95/hello.sbt) created; verification pending |
| `.sc` | [hello.sc](variants/sc-4a5e9bf6/hello.sc) created; verification pending |
