# #591 ROS Interface

Analyze a ROS message interface with constant GREETING and string message field.

Canonical type `data`, language_id `809230569`.

Suggested toolchain: ROS2 rosidl_adapter parser original.

From the example directory:

```sh
python verify.py
```

Expected result: constant and accepted field; constant value Hello, World!.

The declared behavior is the definition of the interface, not a DDS transmission.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + original ROS2 rosidl_adapter source. [Log](verification/result.json).

Sources:

- [ROS interface syntax](https://design.ros2.org/articles/interface_definition.html)
- [rosidl adapter](https://github.com/ros2/rosidl/blob/rolling/rosidl_adapter/rosidl_adapter/parser.py)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.msg` | [Greeting.msg](Greeting.msg) verified |
| `.action` | [hello.action](variants/action-b07b298b/hello.action) created; verification pending |
| `.srv` | [hello.srv](variants/srv-506ca812/hello.srv) created; verification pending |
