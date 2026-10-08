# #592 RPC

Generare XDR da una definizione RPC e serializzare/deserializzare il saluto in memoria.

Tipo canonico `programming`, language_id `1031374237`.

Toolchain prevista: rpcgen, GCC e libtirpc.

Dalla cartella dell’esempio:

```sh
mkdir -p build
rpcgen -h -o build/hello.h hello.x
rpcgen -c -o build/hello_xdr.c hello.x
gcc -Ibuild -I/usr/include/tirpc verify.c build/hello_xdr.c -ltirpc -o build/verify
./build/verify
```

Risultato atteso: XDR codificato e decodificato uguale al saluto.

Non avvia rpcbind o servizi di rete: verifica il codice XDR generato.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: rpcgen1.4.2 + GCC13.3 + libtirpc native XDR. [Log](verification/result.json). 

Fonti:

- [rpcgen](https://man7.org/linux/man-pages/man1/rpcgen.1.html)
- [libtirpc](https://sourceforge.net/projects/libtirpc/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.x` | [hello.x](hello.x) verificato |
