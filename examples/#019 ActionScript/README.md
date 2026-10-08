# #019 ActionScript

`HelloWorld.as` è una classe documento **ActionScript 3** derivata da `Sprite`.
Il costruttore crea un `TextField`, assegna `Hello World` e lo aggiunge alla
lista di visualizzazione. Il saluto compare sullo stage, non nella console.

Toolchain richiesta: compilatore `mxmlc` (Apache Flex SDK con la libreria
`playerglobal.swc` appropriata) e un runtime SWF compatibile. Dalla cartella
dell'esempio, con il compilatore configurato nel PATH, questo comando compila
e controlla la sintassi ActionScript:

```sh
mxmlc -strict=true -output=HelloWorld.swf HelloWorld.as
```

Risultato atteso del controllo sintattico: codice di uscita zero e creazione
di `HelloWorld.swf` senza errori. Questo comando è registrato sia come build
sia come comando di verifica della voce; non verifica da solo il rendering.

Per controllare la semantica occorre aprire il file generato in un runtime SWF
compatibile con ActionScript 3 e osservare il testo `Hello World` sullo stage.
Il comando preciso di esecuzione dipende dal runtime scelto; questa parte
resta da fissare e verificare.

Sintassi e semantica verificate: **no**. Blocchi attuali: compilatore Flex,
`playerglobal.swc` e runtime SWF non disponibili nell'ambiente usato. Un controllo
testuale del sorgente non sostituisce compilazione ed esecuzione.

Riferimenti primari: [compilatori Flex, Apache](https://flex.apache.org/doc/flex/using/flx_mxml_mx.html)
e [TextField, Adobe](https://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.as` | [HelloWorld.as](HelloWorld.as) creato, verifiche pendenti |
