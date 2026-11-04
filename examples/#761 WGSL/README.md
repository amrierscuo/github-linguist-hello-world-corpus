# #761 WGSL

Voce canonica `WGSL`, tipo `programming`, `language_id: 836605993`.

## Goal

Eseguire lo shader compute originale `hello.wgsl`, che scrive i 13 codici ASCII di `Hello, World!` in un buffer storage, e leggere il buffer risultante.

## Toolchain and reproduction

Prova autentica con wgpu-py 0.32.0, wgpu-native 29.0.1.1 e CPython 3.12.3 su Ubuntu 24.04 WSL2 x86_64. Il backend Vulkan è Mesa lavapipe 25.2.8, dispositivo software CPU `llvmpipe (LLVM 20.1.2, 256 bits)`. Non è una misura su hardware GPU fisico.

Installare `wgpu==0.32.0` in un ambiente Python isolato. Occorrono il loader Vulkan e il driver Mesa lavapipe. L'ICD utilizzato nella prova è `/usr/share/vulkan/icd.d/lvp_icd.json`; su un altro sistema verificare il percorso effettivo. `XDG_RUNTIME_DIR` deve indicare una directory privata esistente con permessi 700, esterna al corpus.

From the example directory, with the active Python environment and `XDG_RUNTIME_DIR` configured:

```sh
VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/lvp_icd.json WGPU_BACKEND_TYPE=Vulkan python verify_compute.py
```

`verify_compute.py` richiede un adapter di fallback e controlla che il tipo sia `CPU` e il backend `Vulkan`. Compila una pipeline dal file WGSL, inizializza a zero un buffer storage di 52 byte, esegue un dispatch di un workgroup da 13 invocazioni, sottomette i comandi e legge il buffer con `queue.read_buffer`. Verifica i tredici valori `u32` e stampa il report dell'adapter seguito dal saluto.

The previous static test with Naga 27.0.3 is preserved. It can be repeated with Rust 1.90.0 using `cargo run --locked --manifest-path Cargo.toml -- hello.wgsl`; hold `CARGO_HOME` and `CARGO_TARGET_DIR` out of the corpus.

## Expected result and status

The values read by the buffer are:

```text
72 101 108 108 111 44 32 87 111 114 108 100 33
Hello, World!
```

Artifact created: yes. syntax verified: yes. behavior verified: yes.

Pipeline, dispatch e readback autentici sul dispositivo software CPU terminano con exit code 0. Il sorgente `hello.wgsl` è invariato. Il precedente log Naga è [verification/native.json](verification/native.json); la nuova prova completa è [verification/runtime.json](verification/runtime.json). Sono registrati ambiente, versioni, adapter, comandi, output, codici letti e SHA-256 del sorgente, del driver e delle librerie native utilizzate. I percorsi personali sono sostituiti con placeholder.

The Python driver is verification support and remains excluded from the language statistics through the `verify_*` rule.

## Primary sources

- [Specifica WGSL](https://www.w3.org/TR/WGSL/)
- [Naga](https://github.com/gfx-rs/wgpu/tree/trunk/naga)
- [wgpu-py, compute senza canvas e lettura dei buffer](https://wgpu-py.readthedocs.io/en/stable/guide.html)
- [Distribuzione wgpu 0.32.0](https://pypi.org/project/wgpu/0.32.0/)
- [Mesa, frontend lavapipe software Vulkan](https://docs.mesa3d.org/sourcetree.html)
- [Mesa, selezione del driver Vulkan tramite ICD](https://docs.mesa3d.org/install.html)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.wgsl` | [hello.wgsl](hello.wgsl) syntax and behavior verified |
