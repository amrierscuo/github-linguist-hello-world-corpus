# #071 BlitzMax

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Compilare un’applicazione console BlitzMax con BRL.StandardIO e stampare Hello, World!.

SuperStrict abilita il controllo rigoroso; Framework BRL.StandardIO fornisce l’output console. Non sono necessarie dipendenze grafiche.

## Toolchain e riproduzione

BlitzMax NG con bmk e modulo BRL.StandardIO; versione effettiva da registrare

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bmk makeapp -t console -o hello hello.bmx
```

```text
./hello (su Windows: hello.exe)
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; nessun parser o runtime nativo è stato eseguito per questa voce.

Impedimenti: BlitzMax NG/bmk non disponibile; compilazione ed esecuzione restano da verificare.

## Fonti primarie

- https://blitzmax.org/docs/en/setup/get_started/
- https://blitzmax.org/docs/en/api/brl/brl.standardio/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bmx` | [hello.bmx](hello.bmx) creato, verifiche pendenti |
