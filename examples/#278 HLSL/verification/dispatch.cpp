#include <d3d11.h>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <iterator>
#include <string>

static void check(HRESULT hr, const char* where) {
    if (FAILED(hr)) {
        std::fprintf(stderr, "%s failed: 0x%08lx\n", where, static_cast<unsigned long>(hr));
        std::exit(1);
    }
}

int main(int argc, char** argv) {
    if (argc != 2) return 1;
    std::ifstream file(argv[1], std::ios::binary);
    if (!file) return 1;
    std::string shaderBytecode{std::istreambuf_iterator<char>(file), {}};
    if (shaderBytecode.size() <= 4 || shaderBytecode.substr(0, 4) != "DXBC") return 1;

    D3D_FEATURE_LEVEL level = D3D_FEATURE_LEVEL_11_0;
    ID3D11Device *device = nullptr;
    ID3D11DeviceContext *context = nullptr;
    check(D3D11CreateDevice(nullptr, D3D_DRIVER_TYPE_WARP, nullptr, 0, &level, 1, D3D11_SDK_VERSION, &device, nullptr, &context), "D3D11CreateDevice WARP 11_0");
    ID3D11ComputeShader *shader = nullptr;
    check(device->CreateComputeShader(shaderBytecode.data(), shaderBytecode.size(), nullptr, &shader), "CreateComputeShader");

    constexpr UINT size = 13;
    std::array<uint32_t, size> initial{};
    D3D11_BUFFER_DESC bufferDesc{};
    bufferDesc.ByteWidth = size * sizeof(uint32_t);
    bufferDesc.Usage = D3D11_USAGE_DEFAULT;
    bufferDesc.BindFlags = D3D11_BIND_UNORDERED_ACCESS;
    bufferDesc.MiscFlags = D3D11_RESOURCE_MISC_BUFFER_STRUCTURED;
    bufferDesc.StructureByteStride = sizeof(uint32_t);
    D3D11_SUBRESOURCE_DATA initialData{};
    initialData.pSysMem = initial.data();
    ID3D11Buffer *output = nullptr;
    check(device->CreateBuffer(&bufferDesc, &initialData, &output), "CreateBuffer output");

    D3D11_UNORDERED_ACCESS_VIEW_DESC viewDesc{};
    viewDesc.Format = DXGI_FORMAT_UNKNOWN;
    viewDesc.ViewDimension = D3D11_UAV_DIMENSION_BUFFER;
    viewDesc.Buffer.NumElements = size;
    ID3D11UnorderedAccessView *uav = nullptr;
    check(device->CreateUnorderedAccessView(output, &viewDesc, &uav), "CreateUnorderedAccessView");
    context->CSSetShader(shader, nullptr, 0);
    context->CSSetUnorderedAccessViews(0, 1, &uav, nullptr);
    context->Dispatch(1, 1, 1);
    ID3D11UnorderedAccessView *nullUav = nullptr;
    context->CSSetUnorderedAccessViews(0, 1, &nullUav, nullptr);

    D3D11_BUFFER_DESC copyDesc{};
    copyDesc.ByteWidth = bufferDesc.ByteWidth;
    copyDesc.Usage = D3D11_USAGE_STAGING;
    copyDesc.CPUAccessFlags = D3D11_CPU_ACCESS_READ;
    ID3D11Buffer *copy = nullptr;
    check(device->CreateBuffer(&copyDesc, nullptr, &copy), "CreateBuffer readback");
    context->CopyResource(copy, output);
    D3D11_MAPPED_SUBRESOURCE mapped{};
    check(context->Map(copy, 0, D3D11_MAP_READ, 0, &mapped), "Map readback");

    auto *numbers = static_cast<const uint32_t*>(mapped.pData);
    char result[size + 1]{};
    for (UINT i = 0; i < size; ++i) {
        if (numbers[i] > 127) return 2;
        result[i] = static_cast<char>(numbers[i]);
    }
    context->Unmap(copy, 0);
    copy->Release();
    uav->Release();
    output->Release();
    shader->Release();
    context->Release();
    device->Release();
    std::puts(result);
    return std::strcmp(result, "Hello, World!") == 0 ? 0 : 1;
}
