# #001 1C Enterprise

`hello.os` scrive una riga `Hello, World!` sulla console. La variante scelta è
OneScript, implementazione indipendente del linguaggio BSL di 1C. L'estensione
`.os` è presente nella voce canonica; il nome e i metadati Linguist restano invariati.

## Toolchain e comandi

OneScript **2.2.0**, archivio portabile Windows x64 ufficiale. Estrarre il runtime
in una cartella separata e rendere disponibile `oscript.exe`. Dalla cartella
dell'esempio:

```powershell
oscript -check hello.os
oscript hello.os
```

Non occorre una compilazione separata. Il primo comando deve terminare con codice
0 e `No errors.`; il secondo con codice 0 e una sola riga `Hello, World!`.

## Stato e limiti

Sintassi **verificata** e semantica **verificata** con OneScript 2.2.0 su Windows
x64. La registrazione effettiva, i comandi, i codici di uscita e l'hash del sorgente
sono in `verification/onescript.json`. Il runtime usato è isolato nella cartella
di lavoro esterna al corpus e non è incluso negli esempi.

Questa evidenza copre il dialetto compatibile OneScript. Non è una verifica
eseguita sulla piattaforma commerciale 1C:Enterprise o sulle sue API applicative.

## Fonti primarie

- [Progetto OneScript: linguaggio e `Сообщить`](https://www.oscript.io/).
- [Tutorial ufficiale: esecuzione con `oscript file.os`](https://www.oscript.io/learn/tutorial-info).
- [Release ufficiale e archivio portabile 2.2.0](https://github.com/EvilBeaver/OneScript/releases/tag/v2.2.0).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bsl` | [hello.bsl](variants/ext-bsl-2e62736c/hello.bsl) creato, verifiche pendenti |
| `.os` | [hello.os](hello.os) verificato |
