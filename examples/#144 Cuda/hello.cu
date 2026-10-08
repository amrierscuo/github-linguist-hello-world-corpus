#include <cstdio>
#include <cuda_runtime.h>

__global__ void sayGreeting() {
    if (blockIdx.x == 0 && threadIdx.x == 0) {
        printf("Hello, World!\n");
    }
}

int main() {
    sayGreeting<<<1, 1>>>();
    cudaError_t error = cudaGetLastError();
    if (error == cudaSuccess) error = cudaDeviceSynchronize();
    if (error != cudaSuccess) {
        fprintf(stderr, "%s\n", cudaGetErrorString(error));
        return 1;
    }
    return cudaDeviceReset() == cudaSuccess ? 0 : 1;
}
