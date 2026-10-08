#version 450
layout(vertices=13) out;
layout(location=0) out float greeting_value[];
const uint text[13] = uint[13](72u,101u,108u,108u,111u,44u,32u,87u,111u,114u,108u,100u,33u);
void main() {
 int i=gl_InvocationID;
 greeting_value[gl_InvocationID]=float(text[i])/255.0;
 gl_out[gl_InvocationID].gl_Position=gl_in[i].gl_Position;
 if(i==0) { gl_TessLevelOuter[0]=1.0; gl_TessLevelOuter[1]=1.0; }
}
