# #028 Altium Designer

Sono presenti quattro artefatti originali nei formati ASCII Altium:

- `Hello.PcbDoc`: contorno rettangolare e testo `Hello, World!` sul Top Overlay, altezza40mil e tratto6mil.
- `Hello.SchDoc`: foglio schematico con testo del saluto.
- `Hello.PrjPCB`: progetto con riferimenti ai tre documenti presenti.
- `Hello.OutJob`: output job denominato con il saluto, con generatore Gerber riferito al PCB.

I campi e le strutture seguono il parser/serializer open source `altiumts`. Lo scope è un campione ASCII da importare; la riapertura e la produzione fisica con Altium Designer rimangono da eseguire.

## Riproduzione

Con Node.js20+ e altiumts0.0.89, eseguire `node verify.mjs` per il parsing e le asserzioni dei modelli. Per il controllo nativo aprire/importare il progetto con Altium Designer, verificare testo e documenti, salvare e riaprire; eseguire l'OutJob soltanto in una copia temporanea.

Stato: artefatti creati; sintassi dei quattro modelli ASCII verificata con altiumts0.0.89, round-trip esatto e asserzioni sul saluto/riferimenti riusciti. Semantica nativa Altium ancora in attesa. [Log](verification/altiumts.json). Il parsing open source e il controllo nativo sono distinti.

Fonti: https://github.com/tscircuit/altiumts ; https://github.com/tscircuit/altiumts/blob/main/tests/project-outjob.test.ts ; https://www.altium.com/documentation/altium-designer/tutorial/creating-project-schematic-document

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.OutJob` | [Hello.OutJob](Hello.OutJob) sintassi verificata |
| `.PcbDoc` | [Hello.PcbDoc](Hello.PcbDoc) sintassi verificata |
| `.PrjPCB` | [Hello.PrjPCB](Hello.PrjPCB) sintassi verificata |
| `.SchDoc` | [Hello.SchDoc](Hello.SchDoc) sintassi verificata |
