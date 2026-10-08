#version 450

layout(location = 0) out vec4 pixel;
const int greeting[13] = int[13](72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33);

void main() {
    int index = clamp(int(gl_FragCoord.x), 0, 12);
    float value = float(greeting[index]) / 255.0;
    pixel = vec4(vec3(value), 1.0);
}
