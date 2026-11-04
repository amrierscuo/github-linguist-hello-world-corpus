# 0034 Apex: variant `.cls`

Role: Apex class with static method, not anonymous Apex.

Type: **adapted**. Starting model: examples/#034 Apex/hello.apex; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Compilatore/parser Apex: compilare CorpusGreeting.cls; nell’org di test autorizzata eseguire System.assertEquals('Hello, World!', CorpusGreeting.hello());
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

- [https://github.com/apex-dev-tools/apex-parser](https://github.com/apex-dev-tools/apex-parser)
- [https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html](https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_defining.htm](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_defining.htm)
