# #643 SVG

Render the SVG greeting in Chromium.

## Toolchain

Google Chrome 154.0.8037.98 native SVG renderer

## Procedure

Chrome --headless --screenshot= build/hello.png hello.svg; control text and image.

## Expected result

SVG shows Hello, World! on clear background.

## Status

syntax and behavior verified.

SVG original with text node; no embedded font. The browser interprets the true SVG and produces a screenshot.

Real check 2026-10-08T13:23:05.345487+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.w3.org/TR/SVG2/text.html](https://www.w3.org/TR/SVG2/text.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.svg` | [hello.svg](hello.svg) verified |
