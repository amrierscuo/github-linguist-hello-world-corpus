extends SceneTree

func _initialize() -> void:
    var scene = load("res://hello.tscn") as PackedScene
    if scene == null:
        quit(1)
        return
    var greeting = scene.instantiate() as Label
    if greeting == null or greeting.text != "Hello, World!":
        quit(1)
        return
    print(greeting.text)
    print("PASS: genuine PackedScene loader and Label.text")
    greeting.free()
    quit(0)
