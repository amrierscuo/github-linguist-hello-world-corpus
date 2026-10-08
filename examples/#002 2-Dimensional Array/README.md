# #002 2-Dimensional Array

`hello.2da` è una tabella **2DA V1.0**, variante usata dall'Infinity Engine. La
riga `0` contiene `Hello,` nella colonna `GREETING` e `World!` nella colonna
`TARGET`. È un esempio di dati, quindi non stampa autonomamente un messaggio.
Leggendo i due valori e separandoli con uno spazio si ottiene `Hello, World!`.

L'intestazione identifica il formato; la seconda riga `****` è il valore
predefinito. In questa variante i valori sono separati da spazi e non possono
contenere uno spazio al loro interno: per questo il saluto usa due celle.

## Toolchain e verifica riproducibile

Il percorso di verifica previsto è l'importatore 2DA nativo di **GemRB**, tramite
la sua console Python, con il file disponibile fra le risorse del gioco come
`hello.2da`:

```python
import GemRB
from GUIDefines import GTV_STR
t = GemRB.LoadTable("hello")
greeting = t.GetValue(0, 0, GTV_STR) + " " + t.GetValue(0, 1, GTV_STR)
assert greeting == "Hello, World!"
```

Non c'è un passo di compilazione del file di dati. L'importazione deve riuscire,
con una riga e due colonne, e l'asserzione deve passare. Serve un ambiente GemRB
con risorse/configurazione di gioco. Il file non sostituisce tabelle del gioco:
ha un nome dedicato.

## Stato e limiti

Artefatto creato; sintassi e semantica **non ancora verificate da un lettore 2DA**.
GemRB e un ambiente di gioco non sono disponibili in questa sessione. La
corrispondenza visiva con la specifica non viene conteggiata come validazione.

## Fonti primarie

- [IESDP, specifica di 2DA V1.0](https://gibberlings3.github.io/iesdp/file_formats/ie_formats/2da.htm).
- [GemRB, implementazione dell'importatore 2DA](https://github.com/gemrb/gemrb/blob/master/gemrb/plugins/2DAImporter/2DAImporter.cpp).
- [GemRB, caricamento dei dati tabellari](https://gemrb.org/GUIScript/functions/LoadTable.html).
- [GemRB, lettura delle celle e tipo `GTV_STR`](https://gemrb.org/GUIScript/functions/Table_GetValue.html).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.2da` | [hello.2da](hello.2da) creato, verifiche pendenti |
