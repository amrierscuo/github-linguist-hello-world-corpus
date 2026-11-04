# #339 Jest Snapshot

Read an original Jest snapshot and compare it to the Hello, World! value.

Canonical type `data`, language_id `774635084`.

Suggested toolchain: Node.js 22 and jest-snapshot 30.2.0.

From the example directory:

```sh
node verify.cjs
```

Expected result: snapshot greeting 1 loaded and successful comparison; stdout greeting and LF.

updateSnapshot is none: the checker has to compare the existing file and does not create or update expectations.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + jest-snapshot 30.2.0. [Log](verification/result.json).

Sources:

- [Jest — snapshot testing](https://jestjs.io/docs/snapshot-testing)
- [Jest — implementazione SnapshotState](https://github.com/jestjs/jest/tree/main/packages/jest-snapshot)

Install the dependencies in a separate directory:

```sh
npm install --ignore-scripts --no-audit --no-fund jest-snapshot@30.2.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.snap` | [greeting.test.js.snap](greeting.test.js.snap) verified |
