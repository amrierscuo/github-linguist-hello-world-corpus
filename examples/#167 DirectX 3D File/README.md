# #167 DirectX 3D File

Importare un modello DirectX .x testuale con nodo HelloWorld e un triangolo originale.

## Toolchain

Assimp native importer ------------------------------------------------------ 
Open Asset Import Library ("Assimp", https://github.com/assimp/assimp) 
 -- Commandline toolchain --
------------------------------------------------------ 

Version 5.3 -debug -shared -st (GIT commit 0)

## Comandi e procedura

assimp version; assimp info hello.x

## Risultato atteso

Import exit 0; nodo HelloWorld, una mesh, 3 vertici e una faccia.

## Stato

Sintassi e semantica verificate.

Il saluto è rappresentato dal nome del nodo; questo formato contiene geometria e non stampa testo. FrameTransformMatrix è identità. L’importatore DirectX nativo di Assimp carica davvero il file; la prova riguarda modello e conteggi, senza dichiarare una resa grafica.

Verifica effettiva del 2026-10-08T11:56:11.594568+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://learn.microsoft.com/en-us/windows/win32/direct3d9/x-files--legacy-](https://learn.microsoft.com/en-us/windows/win32/direct3d9/x-files--legacy-)
- [https://github.com/assimp/assimp](https://github.com/assimp/assimp)
- [https://learn.microsoft.com/en-us/windows/win32/direct3d9/mesh](https://learn.microsoft.com/en-us/windows/win32/direct3d9/mesh)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.x` | [hello.x](hello.x) verificato |
