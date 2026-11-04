# #103 Caddyfile

Serve a local HTTP response 200 whose body is exactly Hello, World!.

Canonical type: `data`; `language_id`: `615465151`.

Suggested toolchain: Caddy 2.x. The actual version tried, when available, is in the log.

From the example folder, depending on the PATH:

```sh
caddy validate --config Caddyfile --adapter caddyfile
caddy run --config Caddyfile --adapter caddyfile
```

Expected result: GET http://127.0.0.1:18763/ returns state 200 and 13 byte `Hello, World!`.

The address is only loopback and HTTP; it does not require DNS or certificates. Stop the process with Ctrl+C after request; automatic verification starts and ends its process.

Recorded status: syntax verified; behavior verified. Tried toolchain: Caddy 2.11.7 windows/amd64. See [log](verification/verification.log).

Primary sources or original references of the project:

- [Caddy — direttiva respond](https://caddyserver.com/docs/caddyfile/directives/respond)
- [Caddy — riga di comando](https://caddyserver.com/docs/command-line)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.caddyfile` | [hello.caddyfile](variants/ext-caddyfile-2e636164647966696c65/hello.caddyfile) created; verification pending |
