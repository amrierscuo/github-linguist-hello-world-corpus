# #055 BIRD2

Voce canonica: `BIRD2`, tipo `data`, language_id `584191811`.

Upload a BIRD2 configuration with constant GREETING = Hello, World! and a blackhole route in the internal table; read greetings with the BIRD client.

## Toolchain and reproduction

BIRD 2.14, pacchetto Ubuntu estratto localmente.

BIRD 2.14. Use an Unix socket and an exclusive PID on Linux filesystem. Launch the daemon in a separate session and always end with birdc down.

Commands from the directory of the example; `<output>` indicates a temporary directory external to the corpus.

Terminal 1, from the example folder:

```sh
bird -p -c bird.conf
bird -f -c bird.conf -s /tmp/corpus-bird.sock -P /tmp/corpus-bird.pid
```

Terminal 2, while the daemon of the first terminal is active:

```sh
birdc -s /tmp/corpus-bird.sock eval GREETING
birdc -s /tmp/corpus-bird.sock down
```

Expected result: Parser exit 0; the BIRD client returns the Hello, World! line; isolated daemon finished with exit 0.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The BIRD 2.14 parser accepted the configuration. A daemon with an isolated socket and PID evaluated GREETING through birdc and returned Hello, World!. The configuration uses only static and has no kernel/device protocols, so it does not export routes to the system. Process shutdown was verified.

Real test: [finish.json](verification/finish.json), with UTC, commands, versions, exit code, stdout/stderr and SHA-256 of sources.

## Primary sources

- https://bird.nic.cz/doc/bird-2.14.html
- https://bird.network.cz/doc/bird-3.html
