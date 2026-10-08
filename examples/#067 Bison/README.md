# #067 Bison

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Generare un parser Bison che accetta EOF e stampa Hello, World! tramite l’azione della regola vuota.

La grammatica %empty attiva l’azione al parsing dell’input vuoto. Il lexer restituisce EOF. Il parser C è generato dal tool Bison reale e compilato; gli output generati rimangono fuori dal corpus.

## Toolchain e riproduzione

GNU Bison 3.8.2 tramite WinFlexBison 2.5.25; GNU C 13.3.0 su Ubuntu WSL

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
win_bison -Wall -Werror --output=hello.c hello.bison
gcc -std=c11 -Wall -Wextra hello.c -o hello
```

```text
./hello
```

## Risultato atteso e stato

EOF accettato, stdout esatto Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://www.gnu.org/software/bison/manual/html_node/Empty-Rules.html
- https://github.com/lexxmark/winflexbison/releases/tag/v2.5.25

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bison` | [hello.bison](hello.bison) verificato |
