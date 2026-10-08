# #511 OverPy

Compilare una regola OverPy in Workshop che mostra un big message al giocatore.

Tipo canonico `programming`, language_id `492781155`.

Toolchain prevista: OverPy compiler Node e Overwatch Workshop per esecuzione.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: regola compilata con Big Message e literal Hello, World!; gioco mostra il saluto.

Il compiler è verificabile localmente; l’esecuzione della regola richiede Overwatch. Non è la libreria Python per Overpass.

Stato registrato: sintassi in attesa; semantica in attesa. Toolchain: Node.js 22.20.0 + original OverPy 9.7.17 compiler. [Log](verification/result.json). exit 1: les\overpy\overpy.js:63484:16)
    at new _Ast (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:49568:23)
    at OverPyCompiler.Ast.OverPyDecompiler.Ast (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:49614:10)
    at ${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:48108:55
    at Array.map (<anonymous>)
    at OverPyCompiler.parseLines (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:48108:39)
    at OverPyCompiler.parseLines (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:48351:25)
    at Object.compile (${WORKSPACE}\work\tools_501_520\npm\node_modules\overpy\overpy.js:70876:27)
    at async ${WORKSPACE}\work\staging_501_520\examples\0511_overpy\verify.cjs:5:20 {
  fileStack: [
    {
      name: '<main>',
      path: '/',
      startLine: 2,
      startCol: 5,
      endCol: 22,
      endLine: 2,
      remainingChars: 99999999999,
      staticMember: true,
      fileStackMemberType: 'normal'
    }
  ],
  severity: 'error'
}


Fonti:

- [OverPy original compiler](https://github.com/Zezombye/overpy)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install overpy@9.7.17
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.opy` | [hello.opy](hello.opy) creato, verifiche pendenti |
