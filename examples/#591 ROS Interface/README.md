# #591 ROS Interface

Analizzare una ROS message interface con costante GREETING e campo string message.

Tipo canonico `data`, language_id `809230569`.

Toolchain prevista: ROS2 rosidl_adapter parser originale.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: costante e campo accettati; valore costante Hello, World!.

La semantica dichiarata è la definizione dell’interfaccia, non una trasmissione DDS.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + original ROS2 rosidl_adapter source. [Log](verification/result.json). 

Fonti:

- [ROS interface syntax](https://design.ros2.org/articles/interface_definition.html)
- [rosidl adapter](https://github.com/ros2/rosidl/blob/rolling/rosidl_adapter/rosidl_adapter/parser.py)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.msg` | [Greeting.msg](Greeting.msg) verificato |
| `.action` | [hello.action](variants/action-b07b298b/hello.action) creato, verifiche pendenti |
| `.srv` | [hello.srv](variants/srv-506ca812/hello.srv) creato, verifiche pendenti |
