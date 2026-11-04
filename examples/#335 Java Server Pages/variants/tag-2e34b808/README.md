# 0335: Java Server Pages: `.tag`

Ruolo: JSP tag file dichiarativo con body-content empty e corpo testuale.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OpenJDK 21.0.12 + Apache Tomcat/Jasper 10.1.42 + ECJ 3.33.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Jasper/Tomcat: installare hello.tag in WEB-INF/tags e compilare/renderizzare fixture hello.jsp
```

Expected result: Hello, World! in the local response

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jsp`: `6a749b119df2097106fc0c1a2c12f7eaa2b5bfed03108f62504fb288d71ac721`
- `hello.tag`: `873ac035464e94ac05bf4f07bb8815e2aa91bf2310f75d6c1fd1db6920f3ffde`

Primary sources:

- https://jakarta.ee/specifications/pages/3.1/
- https://tomcat.apache.org/tomcat-10.1-doc/jasper-howto.html
