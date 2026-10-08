name := "corpus-greeting"
version := "1.0.0"
scalaVersion := "2.13.16"
val hello = taskKey[Unit]("Print original greeting")
hello := println("Hello, World!")
