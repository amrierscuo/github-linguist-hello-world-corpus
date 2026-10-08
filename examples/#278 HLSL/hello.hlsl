RWStructuredBuffer<uint> greeting : register(u0);

static const uint text[13] = {72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33};

[numthreads(16, 1, 1)]
void main(uint3 thread : SV_DispatchThreadID) {
    if (thread.x < 13) greeting[thread.x] = text[thread.x];
}
