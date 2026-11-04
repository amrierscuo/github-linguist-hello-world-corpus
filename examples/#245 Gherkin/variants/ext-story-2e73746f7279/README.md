# 0245 Gherkin: variant `.story`

Ruolo: Story JBehave (Scenario/Given/When/Then), distinto dall’header Feature di Gherkin feature.

Type: **adapted**. Starting model: examples/#245 Gherkin/hello.feature; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
JBehave StoryParser: leggere hello.story e collegare step bindings del progetto di test temporaneo.
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

- [https://cucumber.io/docs/gherkin/reference/](https://cucumber.io/docs/gherkin/reference/)
- [https://github.com/cucumber/cucumber-js](https://github.com/cucumber/cucumber-js)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://jbehave.org/reference/stable/story-syntax.html](https://jbehave.org/reference/stable/story-syntax.html)
