# #174 E-mail

Decode an e-mail message RFC 5322/MIME with subject and body Hello, World!.

## Toolchain

Python 3.13.9; stdlib email BytesParser RFC 5322/MIME

## Commands and procedure

python --version; python verify.py

## Expected result

Parser without defects; subject and correct body; SMTP serialization and rereading preserve the body.

## Status

syntax and behavior verified.

All addresses use the example.invalid illustrative domain. The file has newline CRLF and charset UTF - 8. This is a local message test: no e-mail is sent.

Actual verification of 2026-10-08T11:56:14.159762+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://www.rfc-editor.org/rfc/rfc5322](https://www.rfc-editor.org/rfc/rfc5322)
- [https://docs.python.org/3/library/email.parser.html](https://docs.python.org/3/library/email.parser.html)
- [https://docs.python.org/3/library/email.policy.html](https://docs.python.org/3/library/email.policy.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.eml` | [hello.eml](hello.eml) verified |
| `.mbox` | [hello.mbox](variants/ext-mbox-2e6d626f78/hello.mbox) created; verification pending |
