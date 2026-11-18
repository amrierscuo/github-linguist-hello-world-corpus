# #662 Singularity

## Verified on November 18, 2026

The published compatible builder processed the original definition. The runscript from the actual generated SIF filesystem executed in an isolated native container root and printed the exact greeting.

Run `apptainer build greeting.sif Singularity; apptainer sif dump <filesystem partition> greeting.sif; unsquashfs; run /.singularity.d/runscript inside a restricted root filesystem`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Build a container image from a Singularity definition and start the runscript.

Canonical type `programming`, language_id `987024632`.

Suggested toolchain: Apptainer or SingularityCE.

From the example directory:

```sh
apptainer build hello.sif Singularity
apptainer run hello.sif
```

Expected result: Hello, World! and newline printing container runtime.

The construction requires the basic image and a container runtime; the file is not counted as a pure shell script.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Apptainer definition file](https://apptainer.org/docs/user/latest/definition_files.html)

</details>
