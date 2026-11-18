# #176 ECL

## Verified on November 18, 2026

The official native ECL compiler compiled the original workunit. Running it returned the expected scalar greeting.

Run `eclcc -platform=hthor -o hello hello.ecl; ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Return a Hello, World! scale string as OUTPUT result of a HPCC ECL workunit.

## Toolchain

HPCC Systems ECL compiler eclcc e cluster locale; versioni da registrare

## Commands and procedure

eclcc -syntax hello.ecl; perform hello.ecl in the IDE/Playground of the local development cluster and read Results

## Expected result

syntax accepted; result of the workunit contains Hello, World!.

## Status

Syntax and behavioral verification pending.

ECL here means Enterprise Control Language of HPCC Systems. OUTPUT returns a result of the workunit; it does not declare a stdout console.

Remaining requirements:
- eclcc and local HPCC cluster not available; parsing and result workunit pending.

## Primary sources and format reference

- [https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html](https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html)
- [https://hpccsystems.com/training/documentation/learning-ecl/](https://hpccsystems.com/training/documentation/learning-ecl/)
- [https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp](https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ecl` | [hello.ecl](hello.ecl) Syntax and behavior verified |
| `.eclxml` | [hello.eclxml](variants/ext-eclxml-2e65636c786d6c/hello.eclxml) created; verification pending |

</details>
