# #592 RPC

Generate XDR from a RPC definition and serializzare/deserializzare greeting in memory.

Canonical type `programming`, language_id `1031374237`.

Suggested toolchain: rpcgen, GCC and libtirpc.

From the example directory:

```sh
mkdir -p build
rpcgen -h -o build/hello.h hello.x
rpcgen -c -o build/hello_xdr.c hello.x
gcc -Ibuild -I/usr/include/tirpc verify.c build/hello_xdr.c -ltirpc -o build/verify
./build/verify
```

Expected result: XDR encoded and decoded equal to greeting.

It does not start rpcbind or network services: verify the generated XDR code.

Recorded status: syntax verified; behavior verified. Toolchain: rpcgen1.4.2 + GCC13.3 + libtirpc native XDR. [Log](verification/result.json).

Sources:

- [rpcgen](https://man7.org/linux/man-pages/man1/rpcgen.1.html)
- [libtirpc](https://sourceforge.net/projects/libtirpc/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.x` | [hello.x](hello.x) verified |
