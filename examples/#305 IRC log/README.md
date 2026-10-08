# #305 IRC log

Rappresentare un messaggio Hello, World! in un log IRC WeeChat.

## Toolchain

WeeChat logger/backlog; versione da registrare

## Comandi e procedura

Aprire hello.weechatlog nel lettore/backlog di WeeChat; verificare timestamp, prefisso corpus-example e messaggio

## Risultato atteso

Una riga: data/ora, prefisso e saluto, separati da TAB.

## Stato

Sintassi e semantica in attesa.

Fixture testuale originale con data e nickname illustrativi; non proviene da una conversazione reale e non contiene messaggi inviati a utenti. Il formato segue il logger WeeChat; non è un sorgente eseguibile.

Requisiti residui:
- Logger/backlog WeeChat reale non eseguito; verifica del formato con tool nativo pending.

## Fonti primarie

- [https://weechat.org/files/doc/devel/weechat_user.en.html](https://weechat.org/files/doc/devel/weechat_user.en.html)
- [https://github.com/weechat/weechat/tree/main/src/plugins/logger](https://github.com/weechat/weechat/tree/main/src/plugins/logger)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.irclog` | [hello.irclog](variants/irclog-5327b982/hello.irclog) creato, verifiche pendenti |
| `.weechatlog` | [hello.weechatlog](hello.weechatlog) creato, verifiche pendenti |
