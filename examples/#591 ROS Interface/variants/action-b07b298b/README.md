# 0591: ROS Interface: `.action`

Interfaccia ROS action con goal, result e feedback.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.action`.

Control provided, from the folder of the variant:

```text
rosidl_adapter.parser.parse_action_file("corpus_interfaces", Path("hello.action"))
```

Expected result: goal.audience / result.message / feedback.status valid; no robot started.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://design.ros2.org/articles/interface_definition.html](https://design.ros2.org/articles/interface_definition.html)
