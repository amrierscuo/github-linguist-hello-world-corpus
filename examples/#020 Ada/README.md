# #020 Ada

Scrivere Hello World seguito da un a capo usando Ada.Text_IO.Put_Line.

## Riproduzione

Toolchain: GNAT 13.3.0; GCC Ada 13.3.0. Ambiente della prova: Ubuntu 24.04 WSL2 x86_64.

```text
gnatmake hello.adb
./hello
Per .ada: gcc -c -x ada hello.ada -o hello.o; gnatbind hello.ali; gnatlink hello.ali -o hello; ./hello
Per .ads: gnatmake consumer.adb; ./consumer dalla relativa directory variants.
```

Risultato atteso: stdout: Hello World seguito da un a capo; exit 0.

## Verifica

Sintassi e semantica verificate il 2026-10-08T23:32:27.334394+00:00. Le varianti hanno prove separate nel log quando consumate.

[Prova nativa](verification/finish_native.json) contiene versioni, comandi reali, exit code, output e SHA-256. I percorsi locali sono sostituiti da segnaposto. Compilati e dipendenze restano fuori dal corpus.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html](https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html)
- [https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html](https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.adb` | [hello.adb](hello.adb), [consumer.adb](variants/ext-ads-2e616473/consumer.adb) sintassi e semantica verificate |
| `.ada` | [hello.ada](variants/ext-ada-2e616461/hello.ada) sintassi e semantica verificate |
| `.ads` | [greeting.ads](variants/ext-ads-2e616473/greeting.ads) sintassi e semantica verificate |
