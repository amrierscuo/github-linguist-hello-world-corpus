# #516 P4

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
| `.p4` | [hello.p4](hello.p4) created; verification pending |
