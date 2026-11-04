# #645 Sage

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
| `.sage` | [hello.sage](hello.sage) created; verification pending |
| `.sagews` | [hello.sagews](variants/sagews-044b38a6/hello.sagews) created; verification pending |
