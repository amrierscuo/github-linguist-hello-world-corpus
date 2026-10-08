extends SceneTree

func _initialize() -> void:
    var shader := Shader.new()
    shader.code = FileAccess.get_file_as_string("res://hello.gdshader")
    var parameters := shader.get_shader_uniform_list()
    var found := false
    for parameter in parameters:
        if parameter.name == "exposure":
            found = true
    if not found:
        push_error("The native shader compiler did not expose the uniform")
        quit(1)
        return
    print("PASS: native shader compiler exposed exposure uniform")
    quit(0)
