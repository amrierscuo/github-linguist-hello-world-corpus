# #444 Monkey C

Voce canonica `Monkey C`, tipo `programming`, language_id `231751931`.

Launch a Garmin Connect IQ application and write greetings on the simulator console.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede SDK Garmin Connect IQ, device fenix7 e una chiave sviluppatore locale. Il manifest e le risorse PNG/XML sono originali.

Comando/procedura from the directory of the example, unless explicit indications:

```text
monkeyc -f monkey.jungle -d fenix7 -y developer_key.der -o build/greeting.prg; connectiq; monkeydo build/greeting.prg fenix7
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Greeting is a System.println call in the getInitialView path; SDK/simulatore unconfigured. No verification deducted from the only XML.

Remaining requirements:

- Garmin Connect IQ SDK, target-device simulator and local developer signing key are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://developer.garmin.com/connect-iq/connect-iq-basics/your-first-app/](https://developer.garmin.com/connect-iq/connect-iq-basics/your-first-app/)
- [https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mc` | [GreetingApp.mc](source/GreetingApp.mc) created; verification pending |
