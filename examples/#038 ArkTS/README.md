# #038 ArkTS

Mostrare Hello, World! in una pagina ArkUI dichiarativa scritta in ArkTS, con testo centrato verticalmente.

## File

- `Index.ets`

## Toolchain e verifica

DevEco Studio con HarmonyOS SDK ArkTS/ArkUI e progetto Empty Ability, modello Stage, API compatibile >=9. Versioni da registrare sulla toolchain disponibile.

In DevEco Studio creare un progetto **Empty Ability** con modello **Stage**
e SDK ArkTS/ArkUI compatibile (API 9 o successiva). Sostituire la pagina
`entry/src/main/ets/pages/Index.ets` con il file qui presente. Il modello deve
mantenere la pagina Index nell'elenco delle pagine del modulo.

Dalla radice del progetto, per un modulo `entry` e prodotto `default`:

```text
hvigorw assembleHap --mode module -p module=entry@default -p product=default
```

Su Windows usare `hvigorw.bat`; in alternativa usare **Build > Build Hap(s)**
nell'IDE. Poi aprire Previewer per la pagina `@Entry`, oppure eseguire su un
dispositivo o emulatore compatibile. Il valore atteso del componente `Text`
è Hello, World!. Registrare le versioni effettive di DevEco, SDK e Hvigor,
l'esito della compilazione e una prova del testo visualizzato.

Il file è una pagina da integrare nel modello standard, che fornisce
configurazioni, Ability, risorse e toolchain. Non è stato compilato con `tsc`;
le estensioni dichiarative ArkUI richiedono il compilatore ArkTS.

## Risultato atteso

Compilazione ArkTS/ArkUI senza errori; Previewer o dispositivo mostra il componente Text con Hello, World!.

## Stato della prova

Sintassi e semantica in attesa.

Pagina ArkTS da inserire nel progetto standard DevEco. Non è un progetto completo; un compilatore TypeScript non sostituisce quello ArkTS/ArkUI.

Requisiti residui:
- DevEco Studio, HarmonyOS SDK ArkTS/ArkUI e progetto Stage compatibile non disponibili; compilazione e rendering non eseguiti.

## Fonti primarie

- [https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-previewer-arkui-V5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-previewer-arkui-V5)
- [https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-commandline](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-commandline)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ets` | [Index.ets](Index.ets) creato, verifiche pendenti |
