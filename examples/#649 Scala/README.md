# #649 Scala

Compilare Scala ed eseguire main sulla JVM.

## Toolchain

Scala compiler version 2.13.16 -- Copyright 2002-2025, LAMP/EPFL and Lightbend, Inc. dba Akka

## Procedura

scalac Hello.scala -d build; java -cp build:<scala-library.jar> Hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:23:07.902520+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://docs.scala-lang.org/scala3/book/taste-hello-world.html](https://docs.scala-lang.org/scala3/book/taste-hello-world.html)
- [https://github.com/scala/scala/releases/tag/v2.13.16](https://github.com/scala/scala/releases/tag/v2.13.16)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.scala` | [Hello.scala](Hello.scala) verificato |
| `.kojo` | [hello.kojo](variants/kojo-eb37572d/hello.kojo) creato, verifiche pendenti |
| `.sbt` | [hello.sbt](variants/sbt-8cfa3e95/hello.sbt) creato, verifiche pendenti |
| `.sc` | [hello.sc](variants/sc-4a5e9bf6/hello.sc) creato, verifiche pendenti |
