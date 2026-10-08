#version 450
const uint text[13] = uint[13](72u,101u,108u,108u,111u,44u,32u,87u,111u,114u,108u,100u,33u);
layout(location=0) out float greeting_value;
void main() {
 int i=gl_VertexIndex % 13;
 greeting_value=float(text[i])/255.0;
 gl_Position=vec4(float(i)/6.0-1.0,0.0,0.0,1.0);
}
