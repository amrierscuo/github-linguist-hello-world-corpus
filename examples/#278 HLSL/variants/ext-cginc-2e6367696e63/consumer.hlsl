#include "hello.cginc"
RWStructuredBuffer<uint> result : register(u0);
[numthreads(13,1,1)]
void main(uint3 id : SV_DispatchThreadID) { result[id.x] = (uint)round(corpusGreetingValue((int)id.x) * 255.0); }
