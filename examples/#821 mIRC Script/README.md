# #821 mIRC Script

Upload an alias mIRC that writes greeting in the local window.

## Toolchain

mIRC Script runtime

## Procedure

In mIRC caricare hello.mrc con /load -rs; invocare /hello.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

echo -a produces local output; the sample does not send messages or start connections.

Remaining requirements:
- mIRC runtime unavailable.

## Primary sources

- [https://www.mirc.com/help/html/aliases.html](https://www.mirc.com/help/html/aliases.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mrc` | [hello.mrc](hello.mrc) created; verification pending |
