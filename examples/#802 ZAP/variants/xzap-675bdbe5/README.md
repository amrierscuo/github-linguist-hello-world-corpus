# 0802 — `.xzap`

ZAP XZIP esteso generato realmente da ZILF con VERSION XZIP; non ZAP ZIPv3 rinominato. Include assembly data/string originali e sorgente generatore.

Provenienza: produttore/serializzatore originale eseguito, come registrato nel log.

Artefatto principale: `hello.xzap`.

Controllo previsto:

```text
${WORKSPACE}\work\tools_801_820\zilf\bin\zilf.exe --version
${WORKSPACE}\work\tools_801_820\zilf\bin\zapf.exe --version
${WORKSPACE}\work\tools_801_820\zilf\bin\zilf.exe build greeting.zil hello.xzap -S
${WORKSPACE}\work\tools_801_820\zilf\bin\zapf.exe hello.xzap
${WORKSPACE_WSL}/work/tools_301_320/apt-root/usr/games/dfrotz -m hello.z5
```

Risultato atteso: ZAPF assembla XZIP, Frotz esegue story version 5 e stampa Hello, World!.

Stato: creato; sintassi verificata; semantica verificata.

Toolchain osservata: ZILF 1.9; ZAPF 1.9; Frotz 2.54.

Ambito reale: Compilatore ZILF originale produce assembly XZIP, assembler ZAPF rilegge il file consegnato e interprete Frotz esegue il binario reale. Story binary resta sotto work.

Log: `verification/result.json`; SHA-256 di ogni sorgente/supporto della variante, comandi, exit code e output effettivi. Build/cache restano sotto `work/verify_extensions_561_836`.

Fonti primarie:

- [https://github.com/taradinoc/zilf](https://github.com/taradinoc/zilf)
