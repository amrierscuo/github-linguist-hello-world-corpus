# #372 LabVIEW

Sono presenti tre **modelli XML di contenitore**, nelle estensioni canoniche `.lvproj`, `.lvlib`, `.lvclass`. La struttura delle radici `Project`, `Library`, `LVClass` e il campo LVVersion seguono gli esempi pubblici NI. Sono modelli da completare e salvare con LabVIEW, non VI grafici eseguibili.

`Hello.vi` è una dipendenza **ancora da creare**: non viene incluso un file VI fittizio. I riferimenti del progetto e della libreria sono quindi intenzionalmente ancora irrisolti. Il `.lvclass` non contiene dati privati o metodi; richiede completamento nell'editor nativo.

## Procedura richiesta dall'utente

1. Aprire/ricreare il progetto con LabVIEW e creare `Hello.vi` nella stessa cartella.
2. Aggiungere uno string indicator al Front Panel.
3. Inserire una string constant `Hello, World!` nel Block Diagram e collegarla all'indicatore.
4. Salvare il VI e i contenitori con l'IDE; eseguire e controllare il saluto.
5. Se il VI appartiene alla libreria, verificarne l'inclusione nel progetto tramite la libreria e salvare i riferimenti risolti.

Artefatti dei contenitori creati come modelli. **Sintassi LabVIEW e semantica non verificate**. La sola lettura XML non viene conteggiata come verifica LabVIEW.

Fonti: materiale dell'utente e strutture dei contenitori NI in https://github.com/ni/labview-memory-management-tools ; https://www.ni.com/en/support/documentation/supplemental/07/labview-project-file-format.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lvproj` | [Hello.lvproj](Hello.lvproj) creato, verifiche pendenti |
| `.lvclass` | [Hello.lvclass](Hello.lvclass) creato, verifiche pendenti |
| `.lvlib` | [Hello.lvlib](Hello.lvlib) creato, verifiche pendenti |
