# #678 Spline Font Database

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

Native FontForge loaded the original SFD and reported its exact FullName. No glyph or font rendering was tested.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json).

## Extension results

- `.sfd`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

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
| `.sfd` | [hello.sfd](hello.sfd) syntax and behavior verified |

</details>
