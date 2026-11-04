# 0174 E-mail: variant `.mbox`

Role: Mailbox mbox with From_ separator and a RFC 5322 original message, not only a EML file renamed.

Type: **adapted**. Starting model: examples/#174 E-mail/hello.eml; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Python mailbox.mbox("hello.mbox"): leggere il messaggio, controllare Subject e body Hello, World!.
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

- [https://www.rfc-editor.org/rfc/rfc5322](https://www.rfc-editor.org/rfc/rfc5322)
- [https://docs.python.org/3/library/email.parser.html](https://docs.python.org/3/library/email.parser.html)
- [https://docs.python.org/3/library/email.policy.html](https://docs.python.org/3/library/email.policy.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.python.org/3/library/mailbox.html](https://docs.python.org/3/library/mailbox.html)
