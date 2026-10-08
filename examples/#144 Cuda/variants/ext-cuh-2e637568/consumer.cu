#include "hello.cuh"
#include <cuda_runtime.h>
int main() { sayGreeting<<<1,1>>>(); return cudaDeviceSynchronize()==cudaSuccess ? 0 : 1; }
