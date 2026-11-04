# 0470: Nginx: `.nginx`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#470 Nginx/hello.nginxconf.

Required toolchain: Nginx1.24.0 Ubuntu, Python3 della fixture locale. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.nginx; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Accepted configuration; HTTP200/body exact Hello, World!; CLEANUP confirmed.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.nginx`: `41ef8b7f6b42418b067520314e2e5d2a710e0ec8f45adbac64988d5253ec981d`
- `verify.py`: `4726c2a66dd3ec19f94ddb8948571b052d1334f34814986d4c22170e8afba957`

Primary sources:

- https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#return
- https://nginx.org/en/docs/switches.html
