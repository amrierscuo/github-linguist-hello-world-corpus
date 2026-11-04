# #340 JetBrains MPS

The `project/` project comes from the official JetBrains **The Simplest Language** sample, distributed under Apache-2.0. Stores `.mps` models, `.mpl` language definition and `.msd` solution descriptor, with the real concept logs and original references.

La proprietà testuale del nodo sandbox è stata cambiata in `Hello, World!`. Cartelle e nomi dei descriptor sono stati accorciati, aggiornando i percorsi del progetto e conservando model roots, namespace, ID e registri, per evitare percorsi eccessivi su Windows. Il generatore ufficiale usa BaseLanguage per generare una classe Java con `main` e stampare quella proprietà. I sorgenti Java generati e le cache non sono inclusi: vanno rigenerati dall'IDE.

## Reproduction

Aprire `project/` in una versione compatibile di MPS, caricare linguaggio e soluzione, verificare i modelli, rigenerare tutti i moduli ed eseguire la classe sandbox `Hello`. Risultato atteso: `Hello, World!` su stdout.

Artefatto creato da un progetto ufficiale adattato. **Sintassi MPS e semantica non verificate**: nessuna apertura, risoluzione dei concept o generazione nativa eseguita. Il parsing XML non sostituisce questi controlli.

## Provenance and license

https://github.com/JetBrains/MPS/tree/master/samples/_theSimplestLanguage

Copyright JetBrains and contributors. Full license: `LICENSE-JetBrains-MPS-Apache-2.0.txt`. `source_provenance.json` records adaptation and footprints; XML files of the official project retain their structures, without AST invented.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mps` | [main@generator.mps](project/languages/l/generator/template/main%40generator.mps), [behavior.mps](project/languages/l/languageModels/behavior.mps), [editor.mps](project/languages/l/languageModels/editor.mps), [structure.mps](project/languages/l/languageModels/structure.mps), [typesystem.mps](project/languages/l/languageModels/typesystem.mps), [sandbox.mps](project/solutions/s/jetbrains/mps/samples/theSimplestLanguage/sandbox/sandbox.mps) created; verification pending |
| `.mpl` | [Language.mpl](project/languages/l/Language.mpl) created; verification pending |
| `.msd` | [Solution.msd](project/solutions/s/Solution.msd) created; verification pending |
