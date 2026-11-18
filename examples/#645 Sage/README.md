# #645 Sage

## Verified on November 18, 2026

SageMath used its own script loader and preparser to evaluate the exact original file. The Sage runtime printed the expected greeting.

Run `python -c 'from sage.all import *; load("hello.sage")'`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate a file in the SageMath runtime.

## Toolchain

SageMath

## Procedure

sage hello.sage

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- SageMath runtime unavailable; generic Python test not enough.

## Primary sources

- [https://doc.sagemath.org/html/en/tutorial/](https://doc.sagemath.org/html/en/tutorial/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sage` | [hello.sage](hello.sage) Syntax and behavior verified |
| `.sagews` | [hello.sagews](variants/sagews-044b38a6/hello.sagews) created; verification pending |

</details>
