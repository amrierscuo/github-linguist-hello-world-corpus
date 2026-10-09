extends SceneTree

func _initialize() -> void:
    call_deferred("verify_pixels")

func verify_pixels() -> void:
    var args := OS.get_cmdline_user_args()
    var source := "res://hello.gdshader" if args.is_empty() else args[0]
    var shader: Shader = load(source)
    if shader == null:
        push_error("Cannot load original shader")
        quit(1)
        return
    var material := ShaderMaterial.new()
    material.shader = shader
    var viewport := SubViewport.new()
    viewport.size = Vector2i(130, 10)
    viewport.render_target_update_mode = SubViewport.UPDATE_ALWAYS
    root.add_child(viewport)
    var rect := ColorRect.new()
    rect.size = Vector2(130, 10)
    rect.material = material
    viewport.add_child(rect)
    for i in range(3):
        await process_frame
        await RenderingServer.frame_post_draw
    var image := viewport.get_texture().get_image()
    if image == null or image.is_empty():
        push_error("No rendered image")
        quit(1)
        return
    var expected := [72,101,108,108,111,44,32,87,111,114,108,100,33]
    var measured := []
    for i in range(13):
        var pixel := image.get_pixel(i * 10 + 5, 5)
        var channels := [roundi(pixel.r * 255),roundi(pixel.g * 255),roundi(pixel.b * 255)]
        if channels != [expected[i],expected[i],expected[i]]:
            push_error("Pixel %s: got %s expected %s" % [i,channels,expected[i]])
            quit(1)
            return
        measured.append(channels[0])
    var saved := image.save_png("res://rendered.png")
    if saved != OK:
        quit(1)
        return
    print(JSON.stringify({"godot": Engine.get_version_info().string,
        "renderer": RenderingServer.get_video_adapter_name(),
        "shader": source, "pixels": measured,
        "decoded": PackedByteArray(measured).get_string_from_ascii(),
        "image": "rendered.png"}))
    quit(0)
