# #557 Proguard

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Apply ProGuard rules to a real Java fixture and keep the Hello, World! greeting.

hello.pro is the main configuration file. The driver compiles Hello.java and an original jar, invokes ProGuard with the keep rules and then executes the processed jar. The ottimizzazione/offuscamento are disabled to make explicit the goal of the keep rule; binaries remain in work.

## Toolchain and reproduction

ProGuard7.10.0 ufficiale, JDK21 Microsoft

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
javac Hello.java; jar --create --file input.jar --main-class Hello Hello.class; java -jar proguard.jar @hello.pro
```

```text
java -cp output.jar Hello
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.guardsquare.com/manual/configuration/usage
- https://github.com/Guardsquare/proguard/releases/tag/v7.10.0

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pro` | [hello.pro](hello.pro) verified |
