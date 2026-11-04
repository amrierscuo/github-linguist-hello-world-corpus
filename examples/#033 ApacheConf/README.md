# #033 ApacheConf

`httpd.conf` configures a server limited to `127.0.0.1:18033` and makes `www/hello.txt` accessible. Configuration requires DSO event MPM, unixd and authz_core and a utente/gruppo local `apache`.

Before you run the commands, set `CORPUS_ROOT` to the absolute path of this folder, `CORPUS_RUN` to a temporary folder already written created and `APACHE_MODULE_DIR` to the module directory of the same build of Apache. If the distribution uses different names per user and group, adapt them and repeat the tests; registered results refer to the bytes delivered here.

Example for Alpine, initiated by the example folder with root user **nel solo rootfs isolato**:

```sh
export CORPUS_ROOT="$PWD"
export CORPUS_RUN=/scratch/apache
export APACHE_MODULE_DIR=/usr/lib/apache2
mkdir -p "$CORPUS_RUN"
httpd -t -f "$CORPUS_ROOT/httpd.conf"
httpd -f "$CORPUS_ROOT/httpd.conf" -k start
curl --fail --silent --show-error http://127.0.0.1:18033/hello.txt
httpd -f "$CORPUS_ROOT/httpd.conf" -k stop
```

The expected result is `Syntax OK` and a HTTP body of exactly `Hello, World!` with newline. In local control the body is written in the temporary folder and compared bytes by `www/hello.txt`; the server is arrested at the end.

Toolchain: **Apache HTTP Server 2.4.69 in Alpine Linux 3.23.6 x86_64; curl; mod_mpm_event, mod_unixd, mod_authz_core**.

Status: **Sintassi e semantica verificate.**

Evidence: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). The log keeps exit code, stdout and stderr; the machine paths are normalized.

Control detail: the Apache parser, the successful HTTP request and the exact comparison of the body have passed.The external wrapper then ended with exit 32 because the `/dev` temporary binding mount was still occupied at the time of disassembly.This cleaning error is kept in the log and is distinguished from the completed functional tests; the Apache stop had already been required by the control trap.

Final cleanup was verified with exit code 0. No Apache processes belonging to this rootfs and configuration remain, and the temporary `/dev` bind mount is no longer active. The check inspected only paths and processes for the corpus rootfs and did not touch unrelated services or mounts.

Primary sources:

- [Documentazione / sorgente ufficiale 1](https://httpd.apache.org/docs/2.4/programs/httpd.html)
- [Documentazione / sorgente ufficiale 2](https://httpd.apache.org/docs/2.4/mod/core.html)
- [Documentazione / sorgente ufficiale 3](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.apacheconf` | [hello.apacheconf](variants/ext-apacheconf-2e617061636865636f6e66/hello.apacheconf) created; verification pending |
| `.vhost` | [hello.vhost](variants/ext-vhost-2e76686f7374/hello.vhost) created; verification pending |
