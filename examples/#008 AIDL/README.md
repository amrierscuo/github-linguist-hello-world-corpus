# #008 AIDL

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

Native AOSP compiler generated the intended Binder constant, method signature, Stub and Proxy. No Android IPC or service execution was tested.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json). [Earlier evidence](verification.log).

## Extension results

- `.aidl`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

`corpus/hello/IHello.aidl` declares an Android Binder contract: a constant
`GREETING` with `Hello, World!` value and a method that returns a string.
A AIDL contract does not implement the service and does not print a message alone.
The semantic goal of this example is to generate the Binder interface with
That constant and that signature.

## Toolchain and command

It serves the official `aidl` compiler of Android SDK Build Tools.
example folder, with `aidl` in PATH:

```powershell
New-Item -ItemType Directory -Force -Path .build | Out-Null
aidl --lang=java -I. -o .build corpus/hello/IHello.aidl
```

Expected result: `.build/corpus/hello/IHello.java`, without errors; class
generated must contain `GREETING` and `getGreeting()` together with `Stub` / `Proxy`.
For IPC behavior, it also needs to implement `IHello.Stub`, return
`GREETING`, expose it from a service and call it from an Android client.

## Status

created; syntax and behavior **non verificate**. The `aidl` command is not present.
in the PATH of the working environment. The control of existence of files is not coming
counted as validation of the language. See `verification.log`.

## Primary sources

- [Android Developers: definizione e implementazione AIDL](https://developer.android.com/develop/background-work/services/aidl)
- [Android SDK Build Tools](https://developer.android.com/tools/releases/build-tools)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.aidl` | [IHello.aidl](corpus/hello/IHello.aidl) syntax and behavior verified |

</details>
