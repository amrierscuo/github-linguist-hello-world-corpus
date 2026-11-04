# #662 Singularity

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
