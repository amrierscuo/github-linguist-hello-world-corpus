# #196 Erlang

Fill in a Erlang form and call main/0 to print Hello, World!.

Canonical type `programming`, language_id `104`.

Toolchain provided: Erlang/OTP with erlc and erl.

From the example directory:

```sh
mkdir -p build
erlc -o build hello.erl
erl -noshell -pa build -s hello main -s init stop
```

Expected result: exact stdout `Hello, World!\n`, 0. output

~n is the newline format of I:format. The second call init stop ends the VM after greeting.

Recorded status: syntax verified; behavior verified. Toolchain: Erlang OTP 25 / ERTS 13.2.2.5 original compile:file + BEAM runtime. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [Erlang — moduli e output](https://www.erlang.org/doc/system/seq_prog.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.erl` | [hello.erl](hello.erl), [greeting_app.erl](variants/ext-app-2e617070/greeting_app.erl), [greeting_app.erl](variants/ext-app-src-2e6170702e737263/greeting_app.erl), [consumer.erl](variants/ext-hrl-2e68726c/consumer.erl) created; verification pending |
| `.app` | [hello.app](variants/ext-app-2e617070/hello.app) created; verification pending |
| `.app.src` | [hello.app.src](variants/ext-app-src-2e6170702e737263/hello.app.src) created; verification pending |
| `.es` | [hello.es](variants/ext-es-2e6573/hello.es) created; verification pending |
| `.escript` | [hello.escript](variants/ext-escript-2e65736372697074/hello.escript) created; verification pending |
| `.hrl` | [hello.hrl](variants/ext-hrl-2e68726c/hello.hrl) created; verification pending |
| `.xrl` | [hello.xrl](variants/ext-xrl-2e78726c/hello.xrl) created; verification pending |
| `.yrl` | [hello.yrl](variants/ext-yrl-2e79726c/hello.yrl) created; verification pending |
