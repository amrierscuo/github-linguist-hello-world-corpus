# #470 Nginx

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Upload a Nginx configuration and serve Hello, World! via HTTP on loopback.

The main file .nginxconf uses return200 in location/greeting. The driver invokes nginx-t, starts only the dedicated process su127.0.0.1: 18080, compares the body and finally stops the process and checks the closing of the listener. Temporary files and logs remain in the copy in work.

## Toolchain and reproduction

Nginx1.24.0 Ubuntu, Python3 of the local fixture

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python3 verify.py
```

## Expected result and status

Configurazione accettata; HTTP200/body esatto Hello, World!; CLEANUP confermato.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#return
- https://nginx.org/en/docs/switches.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nginx` | [hello.nginx](variants/nginx-50552489/hello.nginx) created; verification pending |
| `.nginxconf` | [hello.nginxconf](hello.nginxconf) verified |
| `.vhost` | [hello.vhost](variants/vhost-a09033b0/hello.vhost) created; verification pending |
