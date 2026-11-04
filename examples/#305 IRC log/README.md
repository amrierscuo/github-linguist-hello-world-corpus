# #305 IRC log

Represent a Hello, World! message in a log IRC WeeChat.

## Toolchain

WeeChat logger/backlog; versione da registrare

## Commands and procedure

Open hello.weechatlog in the lettore/backlog of WeeChat; check timestamps, prefix corpus-example and message

## Expected result

A line: data/ora, prefix and greeting, separated by TAB.

## Status

Syntax and behavioral verification pending.

Original text fixtures with data and illustrative nickname; it does not come from a real conversation and does not contain messages sent to users. The format follows the WeeChat logger; it is not an executable source.

Remaining requirements:
- Logger/backlog WeeChat real not executed; verification of the format with native tool pending.

## Primary sources

- [https://weechat.org/files/doc/devel/weechat_user.en.html](https://weechat.org/files/doc/devel/weechat_user.en.html)
- [https://github.com/weechat/weechat/tree/main/src/plugins/logger](https://github.com/weechat/weechat/tree/main/src/plugins/logger)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.irclog` | [hello.irclog](variants/irclog-5327b982/hello.irclog) created; verification pending |
| `.weechatlog` | [hello.weechatlog](hello.weechatlog) created; verification pending |
