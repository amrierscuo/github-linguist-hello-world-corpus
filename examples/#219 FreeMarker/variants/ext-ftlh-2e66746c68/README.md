# 0219 FreeMarker: variant `.ftlh`

Ruolo: Template FreeMarker HTML con output format e autoescaping espliciti.

Type: **adapted**. Starting model: examples/#219 FreeMarker/hello.ftl; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
FreeMarker Configuration: caricare hello.ftlh e processare con name="World"; controllare il paragrafo HTML.
```

Expected result: <p> Hello, World! </p>

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://freemarker.apache.org/docs/dgui_quickstart_basics.html](https://freemarker.apache.org/docs/dgui_quickstart_basics.html)
- [https://freemarker.apache.org/docs/pgui_quickstart_all.html](https://freemarker.apache.org/docs/pgui_quickstart_all.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://freemarker.apache.org/docs/dgui_misc_autoescaping.html](https://freemarker.apache.org/docs/dgui_misc_autoescaping.html)
