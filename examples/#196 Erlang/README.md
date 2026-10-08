# #196 Erlang

Compilare un modulo Erlang e chiamare main/0 per stampare Hello, World!.

Tipo canonico `programming`, language_id `104`.

Toolchain prevista: Erlang/OTP con erlc ed erl.

Dalla cartella dell’esempio:

```sh
mkdir -p build
erlc -o build hello.erl
erl -noshell -pa build -s hello main -s init stop
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

~n è il formato newline di io:format. La seconda chiamata init stop termina la VM dopo il saluto.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Erlang OTP 25 / ERTS 13.2.2.5 original compile:file + BEAM runtime. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [Erlang — moduli e output](https://www.erlang.org/doc/system/seq_prog.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.erl` | [hello.erl](hello.erl), [greeting_app.erl](variants/ext-app-2e617070/greeting_app.erl), [greeting_app.erl](variants/ext-app-src-2e6170702e737263/greeting_app.erl), [consumer.erl](variants/ext-hrl-2e68726c/consumer.erl) creato, verifiche pendenti |
| `.app` | [hello.app](variants/ext-app-2e617070/hello.app) creato, verifiche pendenti |
| `.app.src` | [hello.app.src](variants/ext-app-src-2e6170702e737263/hello.app.src) creato, verifiche pendenti |
| `.es` | [hello.es](variants/ext-es-2e6573/hello.es) creato, verifiche pendenti |
| `.escript` | [hello.escript](variants/ext-escript-2e65736372697074/hello.escript) creato, verifiche pendenti |
| `.hrl` | [hello.hrl](variants/ext-hrl-2e68726c/hello.hrl) creato, verifiche pendenti |
| `.xrl` | [hello.xrl](variants/ext-xrl-2e78726c/hello.xrl) creato, verifiche pendenti |
| `.yrl` | [hello.yrl](variants/ext-yrl-2e79726c/hello.yrl) creato, verifiche pendenti |
