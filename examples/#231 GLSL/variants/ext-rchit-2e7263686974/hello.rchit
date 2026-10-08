#version 460
#extension GL_EXT_ray_tracing : require
layout(location=0) rayPayloadInEXT float greeting_value;
const uint text[13] = uint[13](72u,101u,108u,108u,111u,44u,32u,87u,111u,114u,108u,100u,33u);
void main() {
 int i=int(gl_LaunchIDEXT.x % 13u);
 greeting_value=float(text[i])/255.0;
}
