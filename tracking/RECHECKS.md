# Verifiche aggiuntive di voci precedenti

8 ottobre 2026: Elixir **0190** ed Erlang **0196**, inizialmente creati con verifiche pendenti, hanno superato compilazione/interpretazione ed esecuzione native. Toolchain: Elixir 1.14.0, Erlang OTP 25 / ERTS 13.2.2.5 da pacchetti originali isolati fuori dal corpus. Entrambi producono esattamente `Hello, World!` seguito da LF; i log nelle cartelle individuali registrano comandi, exit code e SHA-256 degli artefatti.

La compilazione Erlang usa l’API standard `compile:file`, poi la VM BEAM esegue `hello:main/0` e termina. Lo script Elixir è interpretato dal runtime Elixir originale.

Il bundle Darcs **0159** è stato rigenerato con contesto locale e autore illustrativo, applicato a un repository temporaneo nuovo e verificato nuovamente, prima di confezionare il checkpoint 04.

Gli ZIP dei checkpoint già salvati sono snapshot immutabili. Il tracker corrente e gli ZIP successivi includono le nuove prove; i rapporti dei lotti precedenti descrivono gli esiti al momento del checkpoint originale.

Ulteriori controlli dell'8 ottobre 2026:

- **0502 OpenCL**: Clang 18.1.3 ha accettato il kernel in modalità OpenCL C 1.2, con `-fsyntax-only`, exit code 0. La prova è statica; l'esecuzione con un runtime OpenCL rimane in attesa.
- **0542 Pod 6**: Rakudo/MoarVM 2022.12 ha analizzato e renderizzato il documento con `--doc=Text`, producendo il saluto nel testo renderizzato, exit code 0.
- **0661 Simple File Verification**: RHash 1.4.3 ha letto il file SFV e verificato la fixture `greeting.txt`, CRC32 `B4E89E84`, con `Everything OK`, exit code 0. La prova riguarda il formato SFV e l'integrità del contenuto.
- **0668 SmPL**: Coccinelle 1.1.1 ha applicato la patch semantica al C originale; GCC 13.3.0 ha compilato il risultato, poi il programma ha stampato `Hello, World!` con exit code 0.

Le cartelle individuali riportano README, comandi, fonti, versioni, output e impronte. I sorgenti SFV/SmPL sono rimasti byte per byte identici agli esempi creati nei checkpoint precedenti.

In 13 log è stato corretto un suffisso `.dist` aggiunto per errore alla versione di una libreria Python. Ogni versione è stata riletta dal campo `Version` del METADATA originale, verificando lo SHA-256 già registrato; il campo `metadata_correction` documenta la correzione. Esiti, comandi, output, timestamp e impronte dei sorgenti restano quelli della prova effettiva.
