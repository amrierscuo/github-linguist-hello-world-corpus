#version 450
layout(isolines,equal_spacing) in;
layout(location=0) out float greeting_value;
const uint text[13] = uint[13](72u,101u,108u,108u,111u,44u,32u,87u,111u,114u,108u,100u,33u);
void main() {
 int i=clamp(int(gl_TessCoord.x*13.0),0,12);
 greeting_value=float(text[i])/255.0;
 gl_Position=vec4(gl_TessCoord.x*2.0-1.0,0.0,0.0,1.0);
}
