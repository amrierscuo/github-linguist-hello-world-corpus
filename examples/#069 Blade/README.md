# #069 Blade

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Renderizzare un template Blade con audience = World e ottenere il paragrafo Hello, World!.

La fixture carica l’autoloader e bootstrap/app.php, avvia il kernel console e usa il motore Blade::render della framework. L’interpolazione usa l’escaping HTML nativo. Il controllo del risultato non sostituisce il parser Blade.

## Toolchain e riproduzione

Laravel 12.x con PHP compatibile e applicazione configurata; versione effettiva da registrare

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
Copiare hello.blade.php e verify.php nella root di un’app Laravel configurata, poi: php verify.php
```

## Risultato atteso e stato

stdout esatto <p>Hello, World!</p> seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; nessun parser o runtime nativo è stato eseguito per questa voce.

Impedimenti: PHP e un’applicazione Laravel completa non sono preparati in questo ambiente; il motore Blade non è stato eseguito.

## Fonti primarie

- https://laravel.com/docs/12.x/blade

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.blade` | [hello.blade](variants/ext-blade-2e626c616465/hello.blade) creato, verifiche pendenti |
| `.blade.php` | [hello.blade.php](hello.blade.php) creato, verifiche pendenti |
