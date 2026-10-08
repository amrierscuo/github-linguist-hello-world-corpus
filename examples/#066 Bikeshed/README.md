# #066 Bikeshed

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Generare una specifica HTML con una sezione Greeting contenente Hello, World!.

Il file include metadata Bikeshed e markup della specifica. Il tentativo installato è incompleto e si arresta durante gli import Python, prima del parsing del documento.

## Toolchain e riproduzione

Bikeshed ufficiale; tentativo isolato 3.14.6 con Python 3.13.9; toolchain completa da preparare

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
bikeshed spec hello.bs hello.html
```

```text
Aprire hello.html e verificare la sezione #greeting e il paragrafo Hello, World!.
```

## Risultato atteso e stato

Compilazione senza errori; HTML contiene il paragrafo della sezione Greeting.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

Impedimenti: Dipendenze Bikeshed incomplete: import aiofiles non disponibile. L’installazione completa non è terminata nel tempo previsto; nessuna verifica del documento è conteggiata.

## Fonti primarie

- https://github.com/speced/bikeshed
- https://speced.github.io/bikeshed/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bs` | [hello.bs](hello.bs) creato, verifiche pendenti |
