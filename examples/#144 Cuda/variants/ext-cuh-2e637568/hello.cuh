#ifndef CORPUS_CUDA_GREETING
#define CORPUS_CUDA_GREETING
#include <cstdio>
__global__ void sayGreeting() { if (blockIdx.x == 0 && threadIdx.x == 0) printf("Hello, World!\n"); }
#endif
