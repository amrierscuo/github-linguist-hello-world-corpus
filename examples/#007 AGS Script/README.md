# #007 AGS Script

`room1.asc` è uno script di stanza per **Adventure Game Studio (AGS)**. Il
gestore `room_AfterFadeIn` mostra `Hello, World!` nella finestra messaggi dopo
l'ingresso nella stanza. La chiamata è bloccante finché il giocatore chiude il
messaggio.

## Toolchain e comandi

Serve **AGS Editor 3.6.x** e il relativo motore di gioco. Creare un progetto da
un template con una stanza iniziale e il personaggio configurato. Aprire lo
script della stanza iniziale e inserire il contenuto di `room1.asc`.

Nelle proprietà Events della stanza collegare `Enters room after fade-in` alla
funzione `room_AfterFadeIn`. Il nome della funzione da solo non stabilisce il
collegamento per un evento di stanza. Se il template ha già il gestore,
aggiungervi la chiamata `Display` senza definire due funzioni omonime.

Comando reale di compilazione: `Build > Build EXE` nell'AGS Editor. Comando di
esecuzione del gioco compilato su Windows: `Compiled/Windows/<nome_gioco>.exe`,
dove `<nome_gioco>` è il Game file name del progetto host. Deve apparire una
finestra con `Hello, World!` all'ingresso nella stanza, dopo il fade-in.

Il file `.asc` è l'unità di sorgente dell'esempio; questa cartella non contiene
un progetto AGS completo, immagini, stanza binaria o un gioco compilato.

## Stato e limiti

Artefatto creato; sintassi e semantica **non ancora verificate** dal compilatore
e dal motore AGS. Editor, progetto host e risorse non sono disponibili in questa
sessione.

## Fonti ufficiali

- [AGS, funzione `Display`](https://adventuregamestudio.github.io/ags-manual/Globalfunctions_Message.html).
- [AGS, eventi della stanza e `room_AfterFadeIn`](https://adventuregamestudio.github.io/ags-manual/EventTypes.html).
- [AGS, distribuzione e `Build EXE`](https://adventuregamestudio.github.io/ags-manual/DistGame.html).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asc` | [room1.asc](room1.asc), [greeting.asc](variants/ext-ash-2e617368/greeting.asc) creato, verifiche pendenti |
| `.ash` | [hello.ash](variants/ext-ash-2e617368/hello.ash) creato, verifiche pendenti |
