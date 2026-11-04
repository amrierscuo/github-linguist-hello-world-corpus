# #031 Ant Build System

`build.xml` is an Ant project with `hello` default target; the official `echo` task produces greeting.

Prerequisites: Java and Apache Ant 1.10.18. The official binary distribution was compared with the SHA checksum - 512 published by Apache. The test used Microsoft OpenJDK 21.0.12.1 on Windows x64.

```sh
ant -f build.xml -projecthelp
ant -f build.xml -silent hello
```

The first command reads the project to Ant and confirms the default target. The second ends with exit 0 and produces a `Hello, World!` line; the launcher used in the test also emits the `Buildfile: ...` information line. The log reports the Java equivalent commands with `org.apache.tools.ant.launch.Launcher`, `-nouserlib` and `-noclasspath`, which isolate the additional user test.

Toolchain: **Apache Ant 1.10.18; Microsoft OpenJDK 21.0.12.1; Windows x64**.

Status: **Sintassi e semantica verificate.**

Evidence: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). The log keeps exit code, stdout and stderr; the machine paths are normalized.

Primary sources:

- [Documentazione / sorgente ufficiale 1](https://ant.apache.org/manual/Tasks/echo.html)
- [Documentazione / sorgente ufficiale 2](https://ant.apache.org/manual/running.html)
- [Documentazione / sorgente ufficiale 3](https://downloads.apache.org/ant/binaries/apache-ant-1.10.18-bin.zip.sha512)
