# #038 ArkTS

Original ArkTS/ArkUI page showing **Hello, World!** centered.The numbering of the folder remains that of the canonical snapshot; the number in the aggregate dashboard is separated.

## Real Verification

On 2026-10-09, the byte-identical `Index.ets` file was compiled with the official OpenHarmony SDK **5.0.0.71 API 12**, ArkUI compiler `4.9.5-r4` and Node **22.20.0**. The compiler exited with code 0, reported no ArkTS errors, and produced `pages/Index.abc` (4428 bytes).

The native Previewer from the same SDK ran the page and produced a native 720×1280 image with **Hello, World!** centered. The image was inspected directly. The automated inspector reports only the root node, so it is not evidence of the text.

syntax and behavior of the page are **verified**. This test concerns the compilation and rendering of the page; it does not certify HAP packaging, signature, installation on device or a complete project.

[Ricevuta e comandi](verification/native_20261009.json), [immagine originale del Previewer](verification/native-frame.jpg), [log nativo](verification/previewer.log).

## Reproduce from the terminal

Download the Windows/Linux SDK from the official link in the sources and verify SHA-256 `f06a2a8ae38a3cf01c583557f5a4bb1e6e3626df975599aa71f4a59e9af70ecc`. Install the Windows ETS, toolchains and previewer components in a short path. The SDK includes the modified ArkUI compiler, its dependencies and `es2abc`. Do not substitute ordinary TypeScript.

Python 3 and Node are necessary for helpers. Capturing Windows requires `websocket-client`, `pywin32` and Pillow. Store all the directories generated outside the corpus. From the example folder, assign `ARKTS_SDK`, `NODE_EXE` and `ARKTS_WORK` to local routes, with `ARKTS_WORK` external:

```powershell
python verify_native_arkui.py --sdk-root "$env:ARKTS_SDK" --source Index.ets --node "$env:NODE_EXE" --project "$env:ARKTS_WORK" --compile
python verify_native_preview.py --previewer "$env:ARKTS_SDK/previewer/common/bin/Previewer.exe" --output "$env:ARKTS_WORK/native-render" --timeout 45 -- -j "$env:ARKTS_WORK/compiler-output" -url pages/Index -or 720 1280 -cr 720 1280 -device phone -shape rect -av ACE_2_0 -pm Stage -arp "$env:ARKTS_WORK/runtime-resources" -pages main_pages -l en_US -hf false -sd 320
```

The second uses named Windows pipe and WebSocket only local, acquires the original JPEG and stops the process it started. A present frame is not enough to certify the greeting: check the text in the image.

## Primary sources

- [Release e checksum del SDK](https://github.com/openharmony/docs/blob/master/en/release-notes/OpenHarmony-v5.0.0-release.md)
- [SDK originale](https://repo.huaweicloud.com/openharmony/os/5.0.0-Release/ohos-sdk-windows_linux-public.tar.gz)
- [Compilatore ArkUI ufficiale](https://github.com/openharmony/developtools_ace_ets2bundle/tree/OpenHarmony-5.0.0-Release)
- [Previewer ufficiale](https://github.com/openharmony/ide_previewer/tree/OpenHarmony-5.0.0-Release)

## GitHub Languages

The local verification is complete. The ArkTS name recognition in GitHub statistics depends on the Linguist register distributed on the service, separately from compilation and execution.
