# #144 Cuda

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Lanciare un singolo thread CUDA che stampa Hello, World! e sincronizzare il device.

Il saluto viene dal kernel __global__, lanciato con <<<1,1>>>. cudaGetLastError e cudaDeviceSynchronize controllano il lancio ed eseguono il flush dell’output; cudaDeviceReset chiude il contesto. Il programma ritorna errore se il device o il runtime non funzionano.

## Toolchain e riproduzione

NVIDIA CUDA Toolkit/nvcc e GPU CUDA compatibile; versioni effettive da registrare

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
nvcc hello.cu -o hello
```

```text
./hello
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline; lancio e sincronizzazione senza errore.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; parser/compilatore/runtime nativo non è stato eseguito per questa voce.

Impedimenti: nvcc e un ambiente GPU CUDA verificabile non sono preparati; compilazione ed esecuzione device restano pendenti.

## Fonti primarie

- https://docs.nvidia.com/cuda/cuda-programming-guide/index.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cu` | [hello.cu](hello.cu), [consumer.cu](variants/ext-cuh-2e637568/consumer.cu) creato, verifiche pendenti |
| `.cuh` | [hello.cuh](variants/ext-cuh-2e637568/hello.cuh) creato, verifiche pendenti |
