# #197 Euphoria

Eseguire un programma Euphoria che stampa Hello, World! seguito da LF.

Tipo canonico `programming`, language_id `880693982`.

Toolchain prevista: OpenEuphoria 4.1.0, interprete eui.

Dalla cartella dell’esempio:

```sh
eui hello.ex
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

Il descrittore 1 è lo stdout predefinito di Euphoria. Il programma non richiede include o librerie aggiuntive.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: OpenEuphoria 4.1.0 Linux x64. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [OpenEuphoria — Hello World](https://openeuphoria.org/wiki/view/tutHelloWorld.wc)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.e` | [hello.e](variants/ext-e-2e65/hello.e) creato, verifiche pendenti |
| `.ex` | [hello.ex](hello.ex) verificato |
