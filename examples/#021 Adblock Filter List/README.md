# #021 Adblock Filter List

Voce canonica: `Adblock Filter List`, tipo `data`, `language_id: 884614762`.
`hello.txt` è una lista originale Adblock Plus 2.0. Blocca le immagini sotto
`example.org/ads/` e permette `hello-world.png` mediante una regola di eccezione.
Questo è l'equivalente dichiarativo del saluto: consentire la risorsa del saluto.

## Toolchain e riproduzione

Verificato su Windows x64 con Node.js **22.20.0** e motore ufficiale
**adblockpluscore 0.11.1**. Dalla directory di questo esempio:

```powershell
npm --prefix .tools install --no-audit --no-fund --save-exact adblockpluscore@0.11.1
node verify.cjs .tools/node_modules hello.txt
```

Il primo comando prepara una dipendenza locale; `verify.cjs` importa il parser e
il matcher del motore. Non sostituisce la grammatica con un parser del corpus.
Risultato atteso: cinque decisioni corrette — immagine banner bloccata, immagine
saluto consentita, script e richieste fuori percorso/dominio senza corrispondenza —
e `PASS: 2 active filters; 5 engine decisions; invalid-option rejected`.

## Stato ed evidenza

Artefatto creato; sintassi **verificata**; semantica **verificata** nel motore ABP.
Controllo negativo: il parser rifiuta un'opzione inesistente. Il file della lista
include intestazione e commenti; la verifica conta esattamente due filtri attivi.
La prova riguarda il matcher locale; non carica un sito né installa un'estensione.
Nessun requisito residuo per la verifica dichiarata.

Log: [adblockpluscore.json](verification/adblockpluscore.json), con comandi, output,
versioni e SHA-256 degli artefatti. I percorsi della macchina nel log sono
normalizzati secondo `path_normalization`; sorgenti e risultati restano invariati.

## Fonti ufficiali

- [Sintassi dei filtri, eccezioni e opzione image](https://help.adblockplus.org/adblock-plus-help-center/how-to-write-filters).
- [Motore adblockpluscore](https://github.com/adblockplus/adblockpluscore).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.txt` | [hello.txt](hello.txt) verificato |
