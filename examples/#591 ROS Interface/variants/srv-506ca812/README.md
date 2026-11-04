# 0591: ROS Interface: `.srv`

Interfaccia ROS service con richiesta e risposta separate da ---.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.srv`.

Control provided, from the folder of the variant:

```text
rosidl_adapter.parser.parse_service_file("corpus_interfaces", Path("hello.srv"))
```

Expected result: request.audience / response.message fields; a real server could return Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://design.ros2.org/articles/interface_definition.html](https://design.ros2.org/articles/interface_definition.html)
