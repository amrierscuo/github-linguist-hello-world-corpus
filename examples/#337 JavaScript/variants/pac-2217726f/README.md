# 0337: JavaScript: `.pac`

Role: Proxy Auto-Configuration valid: function returns DIRECT, greeting is given separate; it does not change OS proxy.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Parser PAC originale offline: caricare hello.pac e chiamare FindProxyForURL con example.invalid
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.pac`: `47984106a219916b503577a800d7a8727bea4fa908094d45f9aaf9174f60cc63`

Primary sources:

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_PAC_file
- https://nodejs.org/api/console.html#consolelogdata-args
