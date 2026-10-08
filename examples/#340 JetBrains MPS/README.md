# #340 JetBrains MPS

Il progetto `project/` deriva dal campione ufficiale JetBrains **The Simplest Language**, distribuito sotto Apache-2.0. Conserva modelli `.mps`, definizione di linguaggio `.mpl` e descriptor di soluzione `.msd`, con i registri reali dei concept e i riferimenti originali.

La proprietà testuale del nodo sandbox è stata cambiata in `Hello, World!`. Cartelle e nomi dei descriptor sono stati accorciati, aggiornando i percorsi del progetto e conservando model roots, namespace, ID e registri, per evitare percorsi eccessivi su Windows. Il generatore ufficiale usa BaseLanguage per generare una classe Java con `main` e stampare quella proprietà. I sorgenti Java generati e le cache non sono inclusi: vanno rigenerati dall'IDE.

## Riproduzione

Aprire `project/` in una versione compatibile di MPS, caricare linguaggio e soluzione, verificare i modelli, rigenerare tutti i moduli ed eseguire la classe sandbox `Hello`. Risultato atteso: `Hello, World!` su stdout.

Artefatto creato da un progetto ufficiale adattato. **Sintassi MPS e semantica non verificate**: nessuna apertura, risoluzione dei concept o generazione nativa eseguita. Il parsing XML non sostituisce questi controlli.

## Provenienza e licenza

https://github.com/JetBrains/MPS/tree/master/samples/_theSimplestLanguage

Copyright JetBrains e contributori. Licenza completa: `LICENSE-JetBrains-MPS-Apache-2.0.txt`. `source_provenance.json` registra l'adattamento e le impronte; i file XML del progetto ufficiale conservano le loro strutture, senza AST inventati.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mps` | [main@generator.mps](project/languages/l/generator/template/main%40generator.mps), [behavior.mps](project/languages/l/languageModels/behavior.mps), [editor.mps](project/languages/l/languageModels/editor.mps), [structure.mps](project/languages/l/languageModels/structure.mps), [typesystem.mps](project/languages/l/languageModels/typesystem.mps), [sandbox.mps](project/solutions/s/jetbrains/mps/samples/theSimplestLanguage/sandbox/sandbox.mps) creato, verifiche pendenti |
| `.mpl` | [Language.mpl](project/languages/l/Language.mpl) creato, verifiche pendenti |
| `.msd` | [Solution.msd](project/solutions/s/Solution.msd) creato, verifiche pendenti |
