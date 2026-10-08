# #466 NetLinx+ERB

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Renderizzare NetLinx+ERB e ottenere il programma startup con Hello, World!.

ERB.new/result(binding) interpola audience nel template .axs.erb e produce sorgente NetLinx. La prova verifica realmente il renderer ERB; la compilazione/esecuzione NetLinx del risultato resta pendente.

## Toolchain e riproduzione

ERB originale Ruby3.2.3; compiler/runtime NetLinx non preparati

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
ruby render.rb
```

## Risultato atteso e stato

Sorgente renderizzato contiene SEND_STRING0 con Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Compiler/runtime NetLinx non disponibili; semantica del target pendente.

## Fonti primarie

- https://docs.ruby-lang.org/en/3.2/ERB.html
- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.axs.erb` | [hello.axs.erb](hello.axs.erb) sintassi verificata |
| `.axi.erb` | [hello.axi.erb](variants/axi-erb-3273de56/hello.axi.erb) creato, verifiche pendenti |
