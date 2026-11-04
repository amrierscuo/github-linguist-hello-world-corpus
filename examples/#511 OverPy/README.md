# #511 OverPy

## Latest recorded verification

**Syntax verified; behavior pending** on November 4, 2026.

The genuine OverPy compiler emitted an Ongoing - Each Player rule with Big Message for Event Player and the exact greeting. The original member invocation was rejected. Execution in Overwatch remains unverified.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json). [Earlier evidence](verification/result.json).

[Original compiler failure](verification/native_20261104_followup_original_failure.json).

## Extension results

- `.opy`: syntax verified; behavior pending.

<details>
<summary>Original instructions and earlier status</summary>

Compile an OverPy rule into an Overwatch Workshop rule that displays a large message to the player.

Canonical type `programming`, language_id `492781155`.

Suggested toolchain: OverPy compiler Node and Overwatch Workshop for execution.

From the example directory:

```sh
node verify.cjs
```

Expected result: Complete rule with Big Message and literal Hello, World!; game shows greeting.

The compiler is verifiable locally; the execution of the rule requires Overwatch. It is not the Python library for Overpass.

Registered state: syntax and behavioral verification pending. Toolchain: Node.js 22.20.0 + original OverPy 9.7.17 compiler. [Log](verification/result.json). exit 1: les\overpy\overpy.js:63484:16)
    at new _Ast (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:49568:23)
    at OverPyCompiler.Ast.OverPyDecompiler.Ast (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:49614:10)
    at ${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:48108:55
    at Array.map (<anonymous>)
    at OverPyCompiler.parseLines (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:48108:39)
    at OverPyCompiler.parseLines (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:48351:25)
    at Object.compile (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:70876:27)
    at async ${WORKSPACE}\work\staging_501_520\examples\0511_overpy\verify.cjs:5:20 {
  fileStack: [
    {
      name: '<main>',
      path: '/',
      startLine: 2,
      startCol: 5,
      endCol: 22,
      endLine: 2,
      remainingChars: 99999999999,
      staticMember: true,
      fileStackMemberType: 'normal'
    }
  ],
  severity: 'error'
}


Sources:

- [OverPy original compiler](https://github.com/Zezombye/overpy)

Install the dependencies in a separate directory:

```sh
npm install overpy@9.7.17
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.opy` | [hello.opy](hello.opy) syntax verified; behavior pending |

</details>
