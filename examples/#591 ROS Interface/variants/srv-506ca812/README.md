# 0591 — ROS Interface — `.srv`

Interfaccia ROS service con richiesta e risposta separate da ---.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.srv`.

Controllo previsto, dalla cartella della variante:

```text
rosidl_adapter.parser.parse_service_file("corpus_interfaces", Path("hello.srv"))
```

Risultato atteso: campi request.audience/response.message; un server reale potrebbe restituire Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://design.ros2.org/articles/interface_definition.html](https://design.ros2.org/articles/interface_definition.html)
