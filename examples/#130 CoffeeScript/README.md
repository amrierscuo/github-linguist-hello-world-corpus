# #130 CoffeeScript

Voce canonica: `CoffeeScript`, tipo `programming`, `language_id: 63`.

Interpolare il destinatario in una stringa CoffeeScript, compilare in JavaScript e stampare il saluto con Node.

## Toolchain e riproduzione

Official CoffeeScript compiler with Node.js runtime — CoffeeScript version 2.7.0. Ambiente della prova: **Windows x64**.

CoffeeScript 2.7.0 e Node.js 22.20.0. Eseguire i comandi in una copia di lavoro: il corpus non include node_modules o il JavaScript generato.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
npm install --prefix .tools coffeescript@2.7.0; node .tools/node_modules/coffeescript/bin/coffee --compile --output build hello.coffee; node build/hello.js
```

Risultato atteso: Compilazione exit 0; runtime exit 0; Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compilatore CoffeeScript ufficiale ha prodotto il JavaScript dal sorgente .coffee originale. Node ha eseguito quel prodotto separato; non viene riscritto manualmente un equivalente JavaScript come prova.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://coffeescript.org/#installation](https://coffeescript.org/#installation)
- [https://coffeescript.org/#strings](https://coffeescript.org/#strings)
- [https://github.com/jashkenas/coffeescript](https://github.com/jashkenas/coffeescript)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.coffee` | [hello.coffee](hello.coffee) verificato |
| `._coffee` | [hello._coffee](variants/ext-coffee-2e5f636f66666565/hello._coffee) creato, verifiche pendenti |
| `.cake` | [hello.cake](variants/ext-cake-2e63616b65/hello.cake) creato, verifiche pendenti |
| `.cjsx` | [hello.cjsx](variants/ext-cjsx-2e636a7378/hello.cjsx) creato, verifiche pendenti |
| `.coffee.erb` | [hello.coffee.erb](variants/ext-coffee-erb-2e636f666665652e657262/hello.coffee.erb) creato, verifiche pendenti |
| `.iced` | [hello.iced](variants/ext-iced-2e69636564/hello.iced) creato, verifiche pendenti |
