#version 450
layout(points) in;
layout(points,max_vertices=13) out;
layout(location=0) out float greeting_value;
const uint text[13] = uint[13](72u,101u,108u,108u,111u,44u,32u,87u,111u,114u,108u,100u,33u);
void main() {
 for(int i=0;i<13;i++) {
  greeting_value=float(text[i])/255.0;
  gl_Position=vec4(float(i)/6.0-1.0,0.0,0.0,1.0);
  EmitVertex(); EndPrimitive();
 }
}
