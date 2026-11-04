#include <d3d10.h>
#include <d3d10effect.h>
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
static std::string read(const char* name) {
    std::ifstream file(name, std::ios::binary);
    if (!file) std::exit(1);
    return {std::istreambuf_iterator<char>(file), {}};
}
int main() {
    constexpr UINT width = 13;
    auto blob = read("effect.fxo");
    auto vs = read("fullscreen_vs.dxbc");
    ID3D10Device *device = nullptr;
    check(D3D10CreateDevice(nullptr, D3D10_DRIVER_TYPE_WARP, nullptr, 0, D3D10_SDK_VERSION, &device), "D3D10CreateDevice WARP");
    ID3D10Effect *effect = nullptr;
    check(D3D10CreateEffectFromMemory(blob.data(), blob.size(), 0, device, nullptr, &effect), "D3D10CreateEffectFromMemory");
    auto *technique = effect->GetTechniqueByName("CorpusGreeting");
    if (!technique->IsValid()) return 3;
    auto *pass = technique->GetPassByName("GreetingPass");
    if (!pass->IsValid()) return 4;

    ID3D10VertexShader *vertex = nullptr;
    check(device->CreateVertexShader(vs.data(), vs.size(), &vertex), "CreateVertexShader");
    D3D10_RASTERIZER_DESC rasterDesc{};
    rasterDesc.FillMode = D3D10_FILL_SOLID;
    rasterDesc.CullMode = D3D10_CULL_NONE;
    rasterDesc.DepthClipEnable = TRUE;
    ID3D10RasterizerState *raster = nullptr;
    check(device->CreateRasterizerState(&rasterDesc, &raster), "CreateRasterizerState");

    D3D10_TEXTURE2D_DESC desc{};
    desc.Width = width;
    desc.Height = 1;
    desc.MipLevels = 1;
    desc.ArraySize = 1;
    desc.Format = DXGI_FORMAT_R8G8B8A8_UNORM;
    desc.SampleDesc.Count = 1;
    desc.Usage = D3D10_USAGE_DEFAULT;
    desc.BindFlags = D3D10_BIND_RENDER_TARGET;
    ID3D10Texture2D *texture = nullptr;
    check(device->CreateTexture2D(&desc, nullptr, &texture), "CreateTexture2D render target");
    ID3D10RenderTargetView *rtv = nullptr;
    check(device->CreateRenderTargetView(texture, nullptr, &rtv), "CreateRenderTargetView");
    const float black[4] = {};
    device->ClearRenderTargetView(rtv, black);

    check(pass->Apply(0), "GreetingPass.Apply");
    D3D10_VIEWPORT viewport{};
    viewport.Width = width;
    viewport.Height = 1;
    viewport.MaxDepth = 1.0f;
    device->RSSetViewports(1, &viewport);
    device->RSSetState(raster);
    device->IASetPrimitiveTopology(D3D10_PRIMITIVE_TOPOLOGY_TRIANGLELIST);
    device->VSSetShader(vertex);
    device->OMSetRenderTargets(1, &rtv, nullptr);
    device->Draw(3, 0);
    device->OMSetRenderTargets(0, nullptr, nullptr);

    desc.Usage = D3D10_USAGE_STAGING;
    desc.BindFlags = 0;
    desc.CPUAccessFlags = D3D10_CPU_ACCESS_READ;
    ID3D10Texture2D *copy = nullptr;
    check(device->CreateTexture2D(&desc, nullptr, &copy), "CreateTexture2D staging");
    device->CopyResource(copy, texture);
    D3D10_MAPPED_TEXTURE2D mapped{};
    check(copy->Map(0, D3D10_MAP_READ, 0, &mapped), "Map staging");

    auto *pixels = static_cast<const unsigned char*>(mapped.pData);
    char result[width + 1]{};
    for (UINT i = 0; i < width; ++i) {
        unsigned char r = pixels[4*i];
        if (r > 127 || r != pixels[4*i+1] || r != pixels[4*i+2] || pixels[4*i+3] != 255) return 5;
        result[i] = static_cast<char>(r);
    }
    copy->Unmap(0);
    copy->Release();
    texture->Release();
    rtv->Release();
    raster->Release();
    vertex->Release();
    effect->Release();
    device->Release();
    std::puts(result);
    return std::strcmp(result, "Hello, World!") == 0 ? 0 : 1;
}
