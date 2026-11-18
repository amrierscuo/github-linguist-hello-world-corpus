# #631 SELinux Policy

## Verified on November 18, 2026

The original SELinux policy was compiled and linked offline. A query of the resulting binary policy retrieves exactly the three specified permissions.

Run `checkmodule -M -m -C -o corpus_greeting.cil hello.te; secilc -o binary.policy -f contexts base.cil corpus_greeting.cil; sesearch --allow -s unconfined_t -t hello_world_t -c file binary.policy`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

[Earlier evidence](verification/toolchain.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill out a SELinux module that declares hello_world_t.

hello_world_t is the equivalent greeting identifier for a policy. The compiler controls form, types and rule allow; the policy is not loaded into the system.

## Toolchain and reproduction

Checkmodule3.5 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
checkmodule -M -m -o corpus_greeting.mod hello.te
```

## Expected result and status

Filling the form ends with exit0.

Artifact created: yes. syntax verified: yes. behavior verified: no.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

Commitments: Behavior of the not verified policy on a SELinux system; behavior operational pendant.

## Primary sources

- https://github.com/SELinuxProject/selinux-notebook/blob/main/src/modular_policy_statements.md?plain=1

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.te` | [hello.te](hello.te) Syntax and behavior verified |

</details>
