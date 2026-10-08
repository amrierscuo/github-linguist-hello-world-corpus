#include <hip/hip_runtime.h>
#include <cstdio>
#include <cstring>

__global__ void greeting(unsigned char* output) {
    const unsigned char text[13] = {72,101,108,108,111,44,32,87,111,114,108,100,33};
    unsigned index = blockIdx.x * blockDim.x + threadIdx.x;
    if (index < 13) output[index] = text[index];
}

int main() {
    unsigned char* device = nullptr;
    unsigned char host[14] = {};
    if (hipMalloc(&device, 13) != hipSuccess) return 1;
    hipLaunchKernelGGL(greeting, dim3(1), dim3(16), 0, 0, device);
    if (hipGetLastError() != hipSuccess || hipDeviceSynchronize() != hipSuccess) return 2;
    if (hipMemcpy(host, device, 13, hipMemcpyDeviceToHost) != hipSuccess) return 3;
    if (hipFree(device) != hipSuccess) return 4;
    if (std::strcmp(reinterpret_cast<char*>(host), "Hello, World!") != 0) return 5;
    std::puts(reinterpret_cast<char*>(host));
}
