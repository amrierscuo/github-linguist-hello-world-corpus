# #065 Bicep

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Compilare un output Bicep costante greeting = Hello, World!.

La verifica esegue il compilatore e controlla l’output ARM generato. Non richiede credenziali Azure o distribuzione di risorse.

## Toolchain e riproduzione

Microsoft Bicep CLI 0.48.1, Windows x64 ufficiale

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bicep build hello.bicep --outfile hello.json
```

```text
Controllare hello.json: outputs.greeting == {"type":"string","value":"Hello, World!"}.
```

## Risultato atteso e stato

Compilazione exit 0 e output ARM JSON esattamente uguale alla costante richiesta.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://learn.microsoft.com/azure/azure-resource-manager/bicep/outputs
- https://github.com/Azure/bicep/releases

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bicep` | [hello.bicep](hello.bicep), [main.bicep](variants/ext-bicepparam-2e6269636570706172616d/main.bicep) creato, verifiche pendenti |
| `.bicepparam` | [hello.bicepparam](variants/ext-bicepparam-2e6269636570706172616d/hello.bicepparam) creato, verifiche pendenti |
