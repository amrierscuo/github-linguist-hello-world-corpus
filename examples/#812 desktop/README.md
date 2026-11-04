# #812 desktop

The native validator accepted the desktop entry. GLib loaded its greeting name, printf command, and terminal setting. No application was launched.

Canonical type: `data`. Linguist language ID: `412`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with desktop-file-utils and GLib GDesktopAppInfo 2.80.0.

[Recorded commands, outputs and hashes](verification/native_20261104_receipt.json).
[Earlier verification record](verification/result.json).

## Reproduce the check

On Linux, from the example directory, run:

```sh
desktop-file-validate hello.desktop
python3 verification/verify_desktop.py hello.desktop
```

The checker loads the launcher fields with GLib. It does not open a desktop or start the configured command.

## Primary sources

- https://specifications.freedesktop.org/desktop-entry/latest/

## Extension coverage

| Extension | Files | Status |
| --- | --- | --- |
| `.desktop` | [hello.desktop](hello.desktop) | Syntax and behavior verified |
| `.desktop.in` | [hello.desktop.in](variants/desktop-in-8bdb31d7/hello.desktop.in) | Verification pending |
