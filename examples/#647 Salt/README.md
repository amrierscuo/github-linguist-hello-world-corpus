# #647 Salt

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
| `.sls` | [hello.sls](hello.sls) created; verification pending |
