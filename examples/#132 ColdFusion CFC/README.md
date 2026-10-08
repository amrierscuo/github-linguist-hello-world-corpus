# #132 ColdFusion CFC

Voce canonica: `ColdFusion CFC`, tipo `programming`, `language_id: 65`.

Definire il componente CFML Greeting e chiamare hello() dal template di controllo, verificando anche un destinatario diverso.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede un motore CFML con sintassi script component/function. Il file CFC definisce un metodo pubblico con argomento string e default; check.cfm usa new Greeting e lancia una eccezione per risultati inattesi.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
Server Lucee/Adobe ColdFusion locale: servire check.cfm con Greeting.cfc nella stessa directory; curl http://localhost:<porta>/check.cfm
```

Risultato atteso: Componente caricato; hello() restituisce Hello, World!; hello("Reader") restituisce Hello, Reader!; risposta HTTP con il saluto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

La voce canonica CFC è separata dal template ColdFusion. Il saluto è il risultato effettivo di un metodo, e il controllo usa un secondo argomento. Nessuna invocazione del componente è attestata finché il motore manca.

Requisiti residui:

- No Adobe ColdFusion/Lucee engine is configured to load and invoke the component.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://docs.lucee.org/reference/tags/component.html](https://docs.lucee.org/reference/tags/component.html)
- [https://docs.lucee.org/reference/tags/function.html](https://docs.lucee.org/reference/tags/function.html)
- [https://docs.lucee.org/guides/cookbooks/component.html](https://docs.lucee.org/guides/cookbooks/component.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cfc` | [Greeting.cfc](Greeting.cfc) creato, verifiche pendenti |
