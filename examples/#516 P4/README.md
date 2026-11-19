# #516 P4

## Verified on November 19, 2026

The publisher’s compiler built the P4 pipeline after renaming implementation types that conflicted with v1model declarations. BMv2 read one synthetic frame and emitted a frame on port 1 whose first 13 bytes decode to the greeting.

Run `p4c-bm2-ss -o hello.json hello.p4 && python3 run_switch.py`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

[Prior attempt](verification/native_20261119_wave800_prior_attempt.json).

<details>
<summary>Earlier instructions and evidence</summary>

Create a P4 header of 104 bit with payload ASCII of greeting and send it to test port 1.

Canonical type `programming`, language_id `348895984`.

Provided Toolchain: p4c bmv2 backend and BMv2 simple_switch in test network.

From the example directory:

```sh
p4c --target bmv2 --arch v1model hello.p4
```

Expected result: successful compilation; issued package contains Hello, World!.

Do not configure switches or real interfaces; behavior requires an isolated BMv2 harness.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [P4 specification](https://p4.org/p4-spec/docs/P4-16-v1.2.5.html)
- [p4c v1model](https://github.com/p4lang/p4c/blob/main/p4include/v1model.p4)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.p4` | [hello.p4](hello.p4) Syntax and behavior verified |

</details>
