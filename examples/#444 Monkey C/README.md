# #444 Monkey C

Voce canonica `Monkey C`, tipo `programming`, language_id `231751931`.

Avviare una applicazione Garmin Connect IQ e scrivere il saluto sulla console del simulatore.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede SDK Garmin Connect IQ, device fenix7 e una chiave sviluppatore locale. Il manifest e le risorse PNG/XML sono originali.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
monkeyc -f monkey.jungle -d fenix7 -y developer_key.der -o build/greeting.prg; connectiq; monkeydo build/greeting.prg fenix7
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il saluto è una chiamata System.println nel percorso getInitialView; SDK/simulatore non configurati. Nessuna verifica dedotta dal solo XML.

Requisiti residui:

- Garmin Connect IQ SDK, target-device simulator and local developer signing key are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://developer.garmin.com/connect-iq/connect-iq-basics/your-first-app/](https://developer.garmin.com/connect-iq/connect-iq-basics/your-first-app/)
- [https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mc` | [GreetingApp.mc](source/GreetingApp.mc) creato, verifiche pendenti |
