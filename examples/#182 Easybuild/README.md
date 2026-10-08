# #182 Easybuild

Descrivere una ricetta EasyBuild che installa uno script locale hello-world e ne esegue il controllo minimo.

Tipo canonico `data`, language_id `342840477`.

Toolchain prevista: EasyBuild 5.x in Linux, strumenti per moduli d’ambiente.

Dalla cartella dell’esempio:

```sh
eb HelloWorld-1.0.eb --prefix ./build/easybuild
```

Risultato atteso: ricetta accettata; script bin/hello-world installato nel prefisso dedicato; esecuzione stampa `Hello, World!\n`.

Bundle non compila librerie: le istruzioni postinstall producono uno script originale. example.invalid è un URL illustrativo; non viene usato per scaricare sorgenti. Il prefisso di esempio è locale.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [EasyBuild — easyconfig](https://docs.easybuild.io/writing-easyconfig-files/)
- [Bundle easyblock originale](https://github.com/easybuilders/easybuild-easyblocks/blob/develop/easybuild/easyblocks/generic/bundle.py)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.eb` | [HelloWorld-1.0.eb](HelloWorld-1.0.eb) creato, verifiche pendenti |
