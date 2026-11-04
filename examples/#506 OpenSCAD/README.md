# #506 OpenSCAD

Generate a three-dimensional greeting text with OpenSCAD.

Canonical type `programming`, language_id `266`.

Suggested toolchain: OpenSCAD CLI with fonts available.

From the example directory:

```sh
openscad -o hello.stl hello.scad
```

Expected result: successful geometric compilation and extruded text Hello, World!.

The goal requires the geometric engine, not only to recognize the string in the source.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [OpenSCAD text](https://openscad.org/cheatsheet/)
- [OpenSCAD manual text](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Text)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.scad` | [hello.scad](hello.scad) created; verification pending |
