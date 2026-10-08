# #505 OpenRC runscript

Interpretare uno script OpenRC che avvia un servizio dimostrativo e mostra il saluto.

Tipo canonico `programming`, language_id `265`.

Toolchain prevista: OpenRC openrc-run; sh per il controllo grammaticale iniziale.

Dalla cartella dell’esempio:

```sh
sh -n hello
openrc-run hello start
```

Risultato atteso: shell syntax valida; avvio dimostrativo con messaggio Hello, World!.

Lo script resta nel corpus e non viene installato in /etc/init.d. sh -n non prova le funzioni OpenRC.

Stato registrato: sintassi verificata; semantica in attesa. Toolchain: Ubuntu POSIX sh syntax only. [Log](verification/result.json). Sintassi POSIX shell verificata; openrc-run non eseguito. Semantica e funzioni OpenRC pendenti.

Fonti:

- [OpenRC service scripts](https://github.com/OpenRC/openrc/blob/master/service-script-guide.md)
