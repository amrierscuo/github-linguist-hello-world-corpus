# #578 QuakeC

Fill QuakeC and invoke worldspawn in a compatible VM.

## Toolchain

FTEQCC package 3343+svn3400-4; compiler version in stdout

## Procedure

fteqcc; load progs.dat in a compatible VM Quake and call worldspawn.

## Expected result

Compilazione senza errori; worldspawn emette Hello, World! nel runtime Quake.

## Status

syntax verified; behavioral verification pending.

Builtin # 23 is bprint of the VM Quake; the real compiler can check the bytecode, but does not simulate the builtin.

Real check 2026-10-08T13:16:51.441635+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

Remaining requirements:
- Quake VM fixture not available; native execution pending.

## Primary sources

- [https://github.com/fte-team/fteqw](https://github.com/fte-team/fteqw)
- [https://github.com/id-Software/Quake/blob/master/WinQuake/pr_cmds.c](https://github.com/id-Software/Quake/blob/master/WinQuake/pr_cmds.c)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.qc` | [hello.qc](hello.qc) syntax verified |
