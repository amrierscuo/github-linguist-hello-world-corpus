# #027 Alpine Abuild

`APKBUILD` è la ricetta del pacchetto `corpus-hello` 1.0.0-r0. La funzione `check()` confronta il greeting; `package()` installa `hello.sh` come `/usr/bin/corpus-hello`. Il checksum SHA-512 lega la ricetta al sorgente. Il campo URL è un dominio dimostrativo; il pacchetto non dipende da quel sito.

Prerequisiti: Alpine Linux, abuild configurato con una chiave di firma locale, apk-tools, BusyBox e OpenSSL. Preparare una copia temporanea di `APKBUILD` e `hello.sh` in `/corpus/0027`, lasciando documenti e log fuori dalla directory di build. Nel chroot di prova è stato usato `-F` perché l'utente era root nel rootfs isolato e `-d` per saltare l'installazione delle dipendenze generiche `build-base`: questo pacchetto contiene soltanto uno script e i comandi richiesti erano già presenti. Su un normale account Alpine configurato usare `abuild -r`.

```sh
cd /corpus/0027
REPODEST=/packages abuild -F -d
apk --no-network add --allow-untrusted /packages/corpus/x86_64/corpus-hello-1.0.0-r0.apk
cmp /usr/bin/corpus-hello hello.sh
test "$(corpus-hello)" = 'Hello, World!'
corpus-hello
```

`--allow-untrusted` riguarda esclusivamente il pacchetto di prova firmato con la chiave temporanea locale. La procedura prevede build, installazione nel rootfs e confronto dei byte installati. Il tentativo registrato ha raggiunto il timeout durante la build; pertanto le verifiche rimangono pendenti. Le distribuzioni, la chiave e gli APK generati rimangono nella cartella di lavoro e non fanno parte del corpus.

Toolchain: **Alpine Linux 3.23.6 x86_64; abuild 3.16.0-r0; apk-tools; BusyBox /bin/sh**.

Stato: **Sintassi e semantica in attesa.**

Requisito residuo: Abuild nel chroot isolato termina per timeout durante la build; checksum e validazione preliminare compaiono nel log, ma build/installazione non hanno esito completo registrato.

Evidenza: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). Il log conserva exit code, stdout e stderr; i percorsi della macchina sono normalizzati.

Fonti primarie:

- [Documentazione / sorgente ufficiale 1](https://wiki.alpinelinux.org/wiki/APKBUILD_Reference)
- [Documentazione / sorgente ufficiale 2](https://github.com/alpinelinux/abuild/blob/master/APKBUILD.5.scd)
- [Documentazione / sorgente ufficiale 3](https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/x86_64/)
