# Native verification batch: November 4, 2026

Sample bytes were matched against the recorded SHA-256 values before updating any status. The VCL receipt also records the tested newline correction. Behavior checks cover the specific native action described in each receipt.

## Main samples

- **#027 Alpine Abuild**: A fresh native APK build, its check step, an offline installation into a disposable Alpine root, and execution of the byte-identical installed script all passed. [Alpine Linux 3.23.6, abuild 3.16.0-r0 and apk-tools 3.0.8-r0 evidence](../examples/%23027%20Alpine%20Abuild/verification/native_20261104_alpine_receipt.json).
- **#102 Cabal Config**: The official Cabal Setup driver configured and built the original package. Its executable printed Hello, World! [Cabal 3.8.1.0 and GHC 9.4.7 evidence](../examples/%23102%20Cabal%20Config/verification/native_20261104_receipt.json).
- **#278 HLSL**: FXC compiled the compute shader and all three include consumers. Direct3D 11 WARP dispatched each shader and read back the expected greeting. The separate Direct3D 10 Effects check rendered the original effect and decoded the same greeting from its pixels. [Microsoft FXC 10.1, Windows SDK 10.0.26100.0, Direct3D WARP and Zig C++ 0.15.2 evidence](../examples/%23278%20HLSL/verification/native_20261104_hlsl_result.json).
- **#285 HTML+Razor**: The ASP.NET Core MVC view engine rendered the original view, and Blazor HtmlRenderer rendered the original component. Each produced <p>Hello, World!</p> in memory. [.NET SDK 8.0.318 and ASP.NET Core 8.0.21 evidence](../examples/%23285%20HTML%2BRazor/verification/native_20261104_html_razor_result.json).
- **#574 QML**: Qt Quick loaded the original QML and rendered a 320 by 120 frame. The native text item and the visible frame both show Hello, World! [PySide6 6.9.2 and Qt 6.9.2 software Qt Quick evidence](../examples/%23574%20QML/verification/native_20261104_qml_result.json).
- **#663 Slang**: Slang generated C++ from the original compute shader. A native CPU host dispatched it and read back the exact ASCII greeting. [Slang 2026.19 and Zig C++ 0.15.2 evidence](../examples/%23663%20Slang/verification/native_20261104_slang_result.json).
- **#743 VCL**: Native compilation and a loopback HTTP request confirmed status 200 and the exact greeting followed by a newline. The minimal correction uses a VCL long string to emit a real newline. [Varnish 7.1.1 in Ubuntu WSL2 evidence](../examples/%23743%20VCL/verification/native_20261104_vcl_candidate_receipt.json).
- **#812 desktop**: The native validator accepted the desktop entry. GLib loaded its greeting name, printf command, and terminal setting. No application was launched. [desktop-file-utils and GLib GDesktopAppInfo 2.80.0 evidence](../examples/%23812%20desktop/verification/native_20261104_receipt.json).

## Independently checked suffixes

- **#039 AsciiDoc**: `.asciidoc`, `.asc`.
- **#102 Cabal Config**: `.cabal`.
- **#178 EJS**: `.ejs.t`, `.jst`.
- **#260 Go Template**: `.gohtml`, `.html.tmpl`, `.tmpl`, `.tpl`.
- **#270 GraphQL**: `.gql`, `.graphqls`.
- **#272 Groovy**: `.groovy`, `.grt`, `.gtpl`, `.gvy`.
- **#278 HLSL**: `.hlsl`, `.cginc`, `.fxh`, `.hlsli`, `.fx`.
- **#285 HTML+Razor**: `.cshtml`, `.razor`.
- **#333 Java**: `.jav`, `.jsh`.
- **#341 Jinja**: `.j2`, `.jinja2`.
- **#574 QML**: `.qml`.
- **#582 R**: `.rd`.
- **#596 Racket**: `.rktd`, `.rktl`.
- **#663 Slang**: `.slang`.
- **#730 TypeScript**: `.cts`, `.mts`.
- **#743 VCL**: `.vcl`.
- **#789 XQuery**: `.xquery`, `.xq`, `.xql`, `.xqm`, `.xqy`.
- **#812 desktop**: `.desktop`.

Main samples: 539 syntax checks and 512 behavior checks. Extension pairs: 583 syntax checks and 507 behavior checks.
