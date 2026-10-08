# 0591 — ROS Interface — `.action`

Interfaccia ROS action con goal, result e feedback.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.action`.

Controllo previsto, dalla cartella della variante:

```text
rosidl_adapter.parser.parse_action_file("corpus_interfaces", Path("hello.action"))
```

Risultato atteso: goal.audience/result.message/feedback.status validi; nessun robot avviato.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://design.ros2.org/articles/interface_definition.html](https://design.ros2.org/articles/interface_definition.html)
