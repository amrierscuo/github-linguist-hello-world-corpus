#include <metal_stdlib>
using namespace metal;
constant uchar greeting_bytes[13] = {72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33};
kernel void greeting(device uchar* output [[buffer(0)]], uint index [[thread_position_in_grid]])
{
    if (index < 13) output[index] = greeting_bytes[index];
}
