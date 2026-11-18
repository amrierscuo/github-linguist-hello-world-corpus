# #199 F*

## Verified on November 18, 2026

The native F-star compiler type-checked the example after exposing its ML effect through FStar.All. The actual generated OCaml program executed the original standard-library greeting call.

Run `fstar --cache_checked_modules Hello.fst; fstar --codegen OCaml --custard_main Hello.main --odir generated Hello.fst; ocamlc Custard.ml -o hello; ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

[Prior attempt](verification/native_20261118_wave736_prior_attempt.json).

<details>
<summary>Earlier instructions and evidence</summary>

Check the types of an F* function with ML effect that prints Hello, World!, then extract it and execute it.

Canonical type `programming`, language_id `336943375`.

Toolchain provided: F* and backend OCaml with FStar.IO and Z3 compatible library.

From the example directory:

```sh
fstar.exe Hello.fst
```

Expected result: module accepted by typechecker; calling main of the extract module, stdout `Hello, World!\n`.

The documented command verifies the types, but does not run main. OCaml extraction, runtime linking and main call remain a separate test; they are not replaced by a simple search of the string in the file.

Initial state: created; syntax and behavioral verification pending. native toolchain not yet performed: syntax and behavior verifications remain pending.

Sources of linguaggio/formato and original implementations:

- [F* — guida alla toolchain](https://fstar-lang.org/tutorial/book/part1/part1_getting_off_the_ground.html)
- [FStar.IO — interfaccia originale](https://github.com/FStarLang/FStar/blob/master/ulib/FStar.IO.fsti)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fst` | [Hello.fst](Hello.fst), [Hello.fst](variants/ext-fsti-2e66737469/Hello.fst) created; verification pending |
| `.fsti` | [Hello.fsti](variants/ext-fsti-2e66737469/Hello.fsti) created; verification pending |

</details>
