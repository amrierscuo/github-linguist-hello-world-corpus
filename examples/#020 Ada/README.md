# #020 Ada

Write Hello World followed by a boss using Ada.Text_IO.Put_Line.

## Reproduction

Toolchain: GNAT 13.3.0; GCC Ada 13.3.0. Test environment: Ubuntu 24.04 WSL2 x86_64.

```text
gnatmake hello.adb
./hello
Per .ada: gcc -c -x ada hello.ada -o hello.o; gnatbind hello.ali; gnatlink hello.ali -o hello; ./hello
Per .ads: gnatmake consumer.adb; ./consumer dalla relativa directory variants.
```

Expected result: stdout: Hello World followed by a boss; exit 0.

## Verification

syntax and behavior verified 2026-10-08T23:32:27.334394+00:00. The variants have separate evidence in the log when consumed.

[Prova nativa](verification/finish_native.json) contains versions, real commands, exit code, output and SHA-256. The local routes are replaced by placeholders.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html](https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html)
- [https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html](https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.adb` | [hello.adb](hello.adb), [consumer.adb](variants/ext-ads-2e616473/consumer.adb) syntax and behavior verified |
| `.ada` | [hello.ada](variants/ext-ada-2e616461/hello.ada) syntax and behavior verified |
| `.ads` | [greeting.ads](variants/ext-ads-2e616473/greeting.ads) syntax and behavior verified |
