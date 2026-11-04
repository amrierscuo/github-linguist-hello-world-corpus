# 0124 Clojure: variant `.cljc`

Ruolo: Sorgente portabile con reader conditional Clojure/ClojureScript.

Type: **adapted**. Starting model: examples/#124 Clojure/hello.clj; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
clojure hello.cljc; compilare separatamente il ramo cljs con il compiler ClojureScript.
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

- [https://clojure.org/reference/repl_and_main](https://clojure.org/reference/repl_and_main)
- [https://clojure.org/reference/special_forms#let](https://clojure.org/reference/special_forms#let)
- [https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/](https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://clojure.org/reference/reader](https://clojure.org/reference/reader)
