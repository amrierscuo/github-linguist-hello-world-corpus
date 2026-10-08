# #277 HIP

Voce canonica `HIP`, tipo `programming`, language_id `674379998`.

Eseguire un kernel HIP che scrive tredici byte ASCII sulla GPU, copiarli sul lato host e confrontare il saluto.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede HIP/ROCm o il backend NVIDIA compatibile, hipcc e GPU/runtime disponibili. Il codice controlla gli errori di allocazione, lancio, sincronizzazione, copia e rilascio.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
hipcc hello.hip -o build/hello; ./build/hello
```

Risultato atteso: Kernel eseguito; readback esatto Hello, World!; exit 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il saluto deriva dai byte scritti dal kernel. La compilazione come C++ normale ignorerebbe semantica/device HIP e non viene presentata come verifica. Hardware/toolchain assenti.

Requisiti residui:

- HIP compiler, compatible GPU and HIP runtime are not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html)
- [https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/examples.html](https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/examples.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hip` | [hello.hip](hello.hip) creato, verifiche pendenti |
