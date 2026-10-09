# #038 ArkTS

Pagina ArkTS/ArkUI originale che mostra **Hello, World!** centrato. La numerazione della cartella resta quella dello snapshot canonico; il numero nella dashboard aggregata è separato.

## Verifica reale

Il 2026-10-09 il file `Index.ets` byte-identico è stato compilato con il SDK ufficiale OpenHarmony **5.0.0.71 API 12**, compiler ArkUI `4.9.5-r4` e Node **22.20.0**. Il compilatore ha restituito exit 0, nessun errore ArkTS e prodotto `pages/Index.abc` (4428 byte).

Il vero Previewer del medesimo SDK ha eseguito la pagina e prodotto una immagine nativa 720×1280 con **Hello, World!** centrato. L'immagine è stata controllata direttamente. L'inspector automatico contiene solo la radice e non viene presentato come prova del testo.

Sintassi e semantica della pagina sono **verificate**. Questa prova riguarda la compilazione e il rendering della pagina; non certifica packaging HAP, firma, installazione su dispositivo o un progetto completo.

[Ricevuta e comandi](verification/native_20261009.json), [immagine originale del Previewer](verification/native-frame.jpg), [log nativo](verification/previewer.log).

## Riproduzione da terminale

Scaricare il SDK Windows/Linux dal collegamento ufficiale indicato nelle fonti e verificare SHA-256 `f06a2a8ae38a3cf01c583557f5a4bb1e6e3626df975599aa71f4a59e9af70ecc`. Installare i componenti Windows ETS, toolchains e previewer in un percorso breve. Il SDK contiene il compilatore ArkUI modificato, le dipendenze e `es2abc`; non sostituirlo con TypeScript ordinario.

Python 3 e Node sono necessari per i helper. La cattura Windows richiede `websocket-client`, `pywin32` e Pillow. Conservare tutte le directory generate fuori dal corpus. Dalla cartella dell'esempio, assegnare `ARKTS_SDK`, `NODE_EXE` e `ARKTS_WORK` a percorsi locali, con `ARKTS_WORK` esterno:

```powershell
python verify_native_arkui.py --sdk-root "$env:ARKTS_SDK" --source Index.ets --node "$env:NODE_EXE" --project "$env:ARKTS_WORK" --compile
python verify_native_preview.py --previewer "$env:ARKTS_SDK/previewer/common/bin/Previewer.exe" --output "$env:ARKTS_WORK/native-render" --timeout 45 -- -j "$env:ARKTS_WORK/compiler-output" -url pages/Index -or 720 1280 -cr 720 1280 -device phone -shape rect -av ACE_2_0 -pm Stage -arp "$env:ARKTS_WORK/runtime-resources" -pages main_pages -l en_US -hf false -sd 320
```

Il primo helper prepara anche i metadata Stage e le risorse minime del progetto. Il secondo usa named pipe Windows e WebSocket solo locali, acquisisce il JPEG originale e arresta il processo che ha avviato. Un frame presente non basta a certificare il saluto: controllare il testo nell'immagine.

## Fonti primarie

- [Release e checksum del SDK](https://github.com/openharmony/docs/blob/master/en/release-notes/OpenHarmony-v5.0.0-release.md)
- [SDK originale](https://repo.huaweicloud.com/openharmony/os/5.0.0-Release/ohos-sdk-windows_linux-public.tar.gz)
- [Compilatore ArkUI ufficiale](https://github.com/openharmony/developtools_ace_ets2bundle/tree/OpenHarmony-5.0.0-Release)
- [Previewer ufficiale](https://github.com/openharmony/ide_previewer/tree/OpenHarmony-5.0.0-Release)

## GitHub Languages

La verifica locale è completa. Il riconoscimento del nome ArkTS nelle statistiche GitHub dipende dal registro Linguist distribuito sul servizio, separatamente da compilazione ed esecuzione.
