RWStructuredBuffer<uint> output;
static const uint greeting[13] = {72,101,108,108,111,44,32,87,111,114,108,100,33};
[shader("compute")]
[numthreads(13,1,1)]
void main(uint3 id : SV_DispatchThreadID) {
    if (id.x < 13) output[id.x] = greeting[id.x];
}
