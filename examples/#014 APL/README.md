# #014 APL

`hello.apl`, codificato UTF-8, assegna alla quad di output `⎕` la stringa
`Hello, World!`. Il risultato è una riga sul terminale.

## Toolchain e comandi

La verifica usa l'interprete APL autentico **dzaima/APL**, implementato in Java,
al commit `5eb0a4205e27afa6122096a25008474eec562dc0`. È un dialetto APL;
il risultato non implica compatibilità completa con altri interpreti.
Servono Git, JDK e Python per il verificatore. Esempio di preparazione locale
PowerShell, dalla cartella dell'esempio:

```powershell
git clone https://github.com/dzaima/APL .tools/dzaima-apl
git -C .tools/dzaima-apl checkout 5eb0a4205e27afa6122096a25008474eec562dc0
New-Item -ItemType Directory -Force -Path .tools/classes | Out-Null
$sources = Get-ChildItem .tools/dzaima-apl/src/APL -Recurse -Filter *.java | ForEach-Object { '"' + $_.FullName.Replace('\', '/') + '"' }
$sources | Set-Content -Encoding utf8 .tools/sources.txt
javac -encoding UTF-8 -d .tools/classes '@.tools/sources.txt'
jar --create --file .tools/APL.jar --main-class APL.Main -C .tools/classes .
java -jar .tools/APL.jar -f hello.apl
python verify.py --jar .tools/APL.jar
```

La build può emettere un avviso Java sulla deprecazione di `finalize()`;
la build effettuata con OpenJDK 21 è riuscita.

## Verifica eseguita

Sintassi e semantica verificate su Windows tramite l'interprete compilato dal
commit indicato. Il controllo ha osservato codice 0, stderr vuoto e stdout
esattamente `b'Hello, World!\r\n'` su Windows. Il checker accetta un solo
terminatore LF oppure CRLF. `verify.py` avvia Java e
confronta stdout; non interpreta APL. Vedere `verification.log`.
Il codice e il JAR dell'interprete sono esclusi dal corpus.

## Fonti primarie

- [dzaima/APL: repository dell'autore](https://github.com/dzaima/APL)
- [dzaima/APL: build al commit verificato](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/build)
- [dzaima/APL: invocazione -f e lettura UTF-8](https://github.com/dzaima/APL/blob/5eb0a4205e27afa6122096a25008474eec562dc0/src/APL/Main.java)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.apl` | [hello.apl](hello.apl) verificato |
| `.dyalog` | [hello.dyalog](variants/ext-dyalog-2e6479616c6f67/hello.dyalog) creato, verifiche pendenti |
