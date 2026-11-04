# #678 Spline Font Database

Open a Spline Font Database and recover the FullName of the font.

Canonical type `data`, language_id `767169629`.

Suggested toolchain: FontForge.

From the example directory:

```sh
fontforge -lang=ff -c 'Open($1); Print($fullname);' hello.sfd
```

Expected result: FontForge accepts font and FullName Hello, World! law.

The font contains metadata and no glyph: the goal is the font name, not the rendering of greeting.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [FontForge SFD](https://fontforge.org/docs/techref/sfdformat.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sfd` | [hello.sfd](hello.sfd) created; verification pending |
