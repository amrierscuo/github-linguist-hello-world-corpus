# 0335 — Java Server Pages: `.tag`

Ruolo: JSP tag file dichiarativo con body-content empty e corpo testuale.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: OpenJDK 21.0.12 + Apache Tomcat/Jasper 10.1.42 + ECJ 3.33.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Jasper/Tomcat: installare hello.tag in WEB-INF/tags e compilare/renderizzare fixture hello.jsp
```

Risultato atteso: Hello, World! nella risposta locale

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jsp`: `6a749b119df2097106fc0c1a2c12f7eaa2b5bfed03108f62504fb288d71ac721`
- `hello.tag`: `873ac035464e94ac05bf4f07bb8815e2aa91bf2310f75d6c1fd1db6920f3ffde`

Fonti primarie:

- https://jakarta.ee/specifications/pages/3.1/
- https://tomcat.apache.org/tomcat-10.1-doc/jasper-howto.html
