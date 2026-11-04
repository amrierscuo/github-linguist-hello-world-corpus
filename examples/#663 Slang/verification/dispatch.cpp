#include "generated_shader.cpp"
#include <cstdio>
#include <cstring>
int main() {
    uint32_t data[13] = {};
    GlobalParams_0 params = {};
    params.output_0.data = data;
    params.output_0.count = 13;
    ComputeVaryingInput input = {};
    input.startGroupID = uint3(0, 0, 0);
    input.endGroupID = uint3(1, 1, 1);
    main_0(&input, nullptr, &params);
    char result[14] = {};
    for (unsigned int i = 0; i < 13; ++i) {
        if (data[i] > 127) return 2;
        result[i] = static_cast<char>(data[i]);
    }
    std::puts(result);
    return std::strcmp(result, "Hello, World!") == 0 ? 0 : 1;
}
