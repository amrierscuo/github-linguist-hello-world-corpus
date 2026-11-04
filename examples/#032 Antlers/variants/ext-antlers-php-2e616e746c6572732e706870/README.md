# 0032 Antlers: variant `.antlers.php`

Role: View Antlers with PHP content, requires PHP parsing explicitly enabled in Statamic.

Type: **adapted**. Starting model: examples/#032 Antlers/hello.antlers.html; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Statamic: renderizzare hello.antlers.php come vista Antlers nel profilo compatibile, con greeting = "Hello, World!"; confrontare l’output.
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://statamic.dev/frontend/antlers](https://statamic.dev/frontend/antlers)
- [https://statamic.dev/getting-started/requirements](https://statamic.dev/getting-started/requirements)
- [https://github.com/statamic/cms/discussions/8696](https://github.com/statamic/cms/discussions/8696)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://statamic.dev/antlers](https://statamic.dev/antlers)
