# #647 Salt

## Verified on November 5, 2026

The genuine Salt renderer and local state engine loaded the exact hello.sls and ran test.show_notification. Its native state result is true, its comment is exactly Hello, World!, and changes is empty. This notification is a returned state message, not a desktop popup. Work-local configuration/cache/log paths were used; no master, daemon or system configuration was changed.

Run `salt-call --local --config-dir <isolated-config> --skip-grains --no-return-event --out=json state.apply hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate a state Salt showing a local notification.

## Toolchain

Salt local state runtime

## Procedure

salt-call --local --file-root=<cartella> state.apply hello

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Salt renderer/state runtime unavailable; YAML generic does not prove the state.

## Primary sources

- [https://docs.saltproject.io/en/latest/ref/states/all/salt.states.test.html](https://docs.saltproject.io/en/latest/ref/states/all/salt.states.test.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sls` | [hello.sls](hello.sls) Syntax and behavior verified |

</details>
