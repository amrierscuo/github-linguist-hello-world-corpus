# 0033 ApacheConf: variant `.vhost`

Role: Apache configuration: the suffix varies, the directives and the standalone profile of the model remain identical.

Tipo variante: **alias**. Copia byte-identica di examples/#033 ApacheConf/httpd.conf

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
httpd -t -f <percorso-assoluto>/hello.vhost; avviare l’istanza isolata e leggere hello.txt con richiesta loopback.
```

Expected result: Syntax OK and exit 0; HTTP successful request with body exactly Hello, World! followed by newline.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://httpd.apache.org/docs/2.4/programs/httpd.html](https://httpd.apache.org/docs/2.4/programs/httpd.html)
- [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/core.html)
- [https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
