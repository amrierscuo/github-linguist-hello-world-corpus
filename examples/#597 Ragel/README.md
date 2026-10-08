# #597 Ragel

Generare una macchina a stati Ragel che accetta il saluto e controllare lo stato finale.

Tipo canonico `programming`, language_id `317`.

Toolchain prevista: Ragel e GCC.

Dalla cartella dell’esempio:

```sh
mkdir -p build
ragel -C -o build/hello.c hello.rl
gcc build/hello.c -o build/hello
./build/hello
```

Risultato atteso: macchina generata raggiunge stato finale dopo tutto l’input.

Il controllo C usa lo stato del codice realmente generato da Ragel.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Ragel 6.10 + GCC 13.3 native Ubuntu. [Log](verification/result.json). 

Fonti:

- [Ragel manual](https://www.colm.net/files/ragel/ragel-guide-6.10.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rl` | [hello.rl](hello.rl) verificato |
