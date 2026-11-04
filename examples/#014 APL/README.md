# #014 APL

`hello.apl`, encoded UTF - 8, assigns the string to the `⎕` output quad
`Hello, World!`. The result is a line on the terminal.

## Toolchain and commands

The verification uses the authentic APL interpreter **dzaima/APL**, implemented in Java,
to commit `5eb0a4205e27afa6122096a25008474eec562dc0`. It is a dialect APL;
the result does not imply complete compatibility with other interpreters.
They serve Git, JDK and Python for the Verifier.
PowerShell, from the example folder:

```powershell
git clone https://github.com/dzaima/APL .tools/dzaima-apl
git -C .tools/dzaima-apl checkout 5eb0a4205e27afa6122096a25008474eec562dc0
New-Item -ItemType Directory -Force -Path .tools/classes | Out-Null
$sources = Get-ChildItem .tools/dzaima-apl/src/APL -Recurse -Filter *.java | ForEach-Object { '"' + $_.FullName.Replace('\', '/') + '"' }
$sources | Set-Content -Encoding utf8 .tools/sources.txt
javac -encoding UTF-8 -d .tools/classes '@.tools/sources.txt'
jar --create --file .tools/APL.jar --main-class APL.Main -C .tools/classes .
java -jar .tools/APL.jar -f hello.apl
python verify.py --jar .tools/APL.jar
```

The build can issue a Java notice on the deprecation of `finalize()`;
the build carried out with OpenJDK 21 has succeeded.

## Verification performed

syntax and behavior verified on Windows through the compiled interpreter
The control has observed code 0, stderr vacuum and stdout
exactly `b'Hello, World!\r\n'` on Windows. The checker accepts only one
terminatore LF oppure CRLF. `verify.py` avvia Java e
compare stdout; do not interpret APL. See `verification.log`.
The interpreter's code and JAR are excluded from the corpus.

## Primary sources

- [dzaima/APL: repository dell'autore](https://github.com/dzaima/APL)
- [dzaima/APL: build al commit verificato](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/build)
- [dzaima/APL: invocazione -f e lettura UTF-8](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/src/APL/Main.java)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.apl` | [hello.apl](hello.apl) verified |
| `.dyalog` | [hello.dyalog](variants/ext-dyalog-2e6479616c6f67/hello.dyalog) created; verification pending |
