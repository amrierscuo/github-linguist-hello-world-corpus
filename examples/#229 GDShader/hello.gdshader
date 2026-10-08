shader_type canvas_item;

uniform float exposure = 1.0;
const int greeting[13] = {72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33};

void fragment() {
    int index = clamp(int(UV.x * 13.0), 0, 12);
    float value = float(greeting[index]) / 255.0;
    COLOR = vec4(vec3(value * exposure), 1.0);
}
