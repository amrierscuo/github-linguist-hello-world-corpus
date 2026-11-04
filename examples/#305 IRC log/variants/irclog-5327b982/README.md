# 0305: IRC log: `.irclog`

Ruolo: Trascrizione IRC testuale offline in formato timestamp/nickname; nessuna sessione o messaggio reale.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: WeeChat logger/backlog; versione da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Aprire il transcript come testo UTF-8; verificare struttura [HH:MM:SS] <nick> messaggio
```

Expected result: A line with illustrative nickname and Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.irclog`: `edd45d668d6d4f44d6f6c3f38cd85528e56e258ef96554560ba9a1ff1ef1101c`

Primary sources:

- https://github.com/github-linguist/linguist/tree/main/samples/IRC%20log
- https://weechat.org/files/doc/devel/weechat_user.en.html
- https://github.com/weechat/weechat/tree/main/src/plugins/logger
