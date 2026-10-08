# #012 ANTLR

`Hello.g4` definisce una grammatica ANTLR 4 che riconosce il saluto letterale
`Hello, World!`, eventuale spazio bianco e la fine dell'input. ANTLR è un linguaggio
per grammatiche: l'obiettivo semantico è riconoscere il messaggio, non attribuire
alla grammatica un'istruzione di stampa. `hello.txt` è l'input e `CheckHello.java`
è un verificatore che usa il lexer e il parser realmente generati da ANTLR.

## Toolchain e comandi

Servono JDK 11+ e il JAR completo ANTLR 4.13.2 dalla pagina ufficiale. Dalla
cartella dell'esempio, impostare `$AntlrJar` al percorso del JAR e lanciare:

```powershell
New-Item -ItemType Directory -Force -Path .build | Out-Null
java -jar $AntlrJar -Werror -o .build Hello.g4
javac -encoding UTF-8 -cp $AntlrJar -d .build .build/HelloLexer.java .build/HelloParser.java .build/HelloListener.java .build/HelloBaseListener.java CheckHello.java
java -cp ".build;$AntlrJar" CheckHello hello.txt
```

Su Linux/macOS il separatore del classpath è `:` invece di `;`.

## Verifica eseguita

Sintassi e semantica verificate con ANTLR 4.13.2 e OpenJDK 21 su Windows.
La generazione con `-Werror` e la compilazione Java sono riuscite. Risultato:

```text
(message Hello, World! <EOF>)
Negative controls rejected: wrong greeting, trailing text, empty input
```

Il verificatore controlla gli errori sia del lexer sia del parser, il contenuto
dell'albero e tre input negativi. I file generati e il JAR restano fuori dal corpus;
vedere `verification.log` per comandi, origine e impronta della toolchain.

## Fonti primarie

- [ANTLR: download ufficiale 4.13.2](https://www.antlr.org/download.html)
- [ANTLR: avvio, generazione e compilazione](https://github.com/antlr/antlr4/blob/4.13.2/doc/getting-started.md)
- [ANTLR: regole del parser](https://github.com/antlr/antlr4/blob/4.13.2/doc/parser-rules.md)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.g4` | [Hello.g4](Hello.g4) verificato |
