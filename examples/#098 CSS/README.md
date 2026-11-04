# #098 CSS

Generate Hello, World! in the pseudo-element CSS: .hello before and apply the color # 123456 in the support page.

## Toolchain

Node.js v22.20.0; css-tree 3.2.1; Google Chrome 154.0.8037.98 (installed file ProductVersion)

## Commands and procedure

From this folder:

```sh
npm install
node check.cjs
```

Open hello.html in the browser. The page script reads the styles
calculated by:before and makes them inspectable in the data-* attributes of the body.
In the Chrome test it was started in headless mode with temporary profile;
the final DOM test the content value and the calculated color.
generated must come from the CSS rule, not from the text of the HTML paragraph.

## Expected result

Parser without errors and valid declarations; browser solves content= "Hello, World!" and color=rgb( 18, 52, 86 ).

## Status

syntax and behavior verified.

hello.html uploads CSS and records the actual browser values in data-generated-content and data-generated-color. The verification uses real Chrome with temporary profile, as well as the parser CSS Tree; it does not declare a screenshot comparison.

Actual verification of 2026-10-08T11:33:51.391848+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://github.com/csstree/csstree](https://github.com/csstree/csstree)
- [https://www.w3.org/TR/css-content-3/](https://www.w3.org/TR/css-content-3/)
- [https://developer.chrome.com/docs/chromium/headless](https://developer.chrome.com/docs/chromium/headless)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.css` | [hello.css](hello.css) verified |
