# #031 Ant Build System

`build.xml` è un progetto Ant con target predefinito `hello`; il task ufficiale `echo` produce il greeting.

Prerequisiti: Java e Apache Ant 1.10.18. La distribuzione binaria ufficiale è stata confrontata con il checksum SHA-512 pubblicato da Apache. La prova ha usato Microsoft OpenJDK 21.0.12.1 su Windows x64.

```sh
ant -f build.xml -projecthelp
ant -f build.xml -silent hello
```

Il primo comando fa leggere il progetto ad Ant e conferma il target predefinito. Il secondo termina con exit 0 e produce una riga `Hello, World!`; il launcher usato nella prova emette anche la riga informativa `Buildfile: ...`. Il log riporta i comandi Java equivalenti con `org.apache.tools.ant.launch.Launcher`, `-nouserlib` e `-noclasspath`, che isolano la prova da librerie utente aggiuntive.

Toolchain: **Apache Ant 1.10.18; Microsoft OpenJDK 21.0.12.1; Windows x64**.

Stato: **Sintassi e semantica verificate.**

Evidenza: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). Il log conserva exit code, stdout e stderr; i percorsi della macchina sono normalizzati.

Fonti primarie:

- [Documentazione / sorgente ufficiale 1](https://ant.apache.org/manual/Tasks/echo.html)
- [Documentazione / sorgente ufficiale 2](https://ant.apache.org/manual/running.html)
- [Documentazione / sorgente ufficiale 3](https://downloads.apache.org/ant/binaries/apache-ant-1.10.18-bin.zip.sha512)
