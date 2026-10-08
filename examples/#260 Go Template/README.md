# #260 Go Template

Eseguire un Go Template che interpola Recipient e produce Hello, World!, controllando HTML escaping.

## Toolchain

go version go1.27.1 windows/amd64

## Comandi e procedura

go version; go run render.go

## Risultato atteso

World produce Hello, World! più newline; <world> produce Hello, &lt;world&gt;! più newline.

## Stato

Sintassi e semantica verificate.

render.go usa html/template.ParseFiles ed Execute del runtime Go, senza tradurre a mano le azioni. La named template greeting e la relativa invocazione sono valutate; l’input aggiuntivo controlla escaping. Il checker è supporto, hello.gotmpl è il campione canonico.

Verifica effettiva del 2026-10-08T12:16:16.831119+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://pkg.go.dev/html/template](https://pkg.go.dev/html/template)
- [https://pkg.go.dev/text/template#hdr-Actions](https://pkg.go.dev/text/template#hdr-Actions)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gohtml` | [hello.gohtml](variants/ext-gohtml-2e676f68746d6c/hello.gohtml) creato, verifiche pendenti |
| `.gotmpl` | [hello.gotmpl](hello.gotmpl) verificato |
| `.html.tmpl` | [hello.html.tmpl](variants/ext-html-tmpl-2e68746d6c2e746d706c/hello.html.tmpl) creato, verifiche pendenti |
| `.tmpl` | [hello.tmpl](variants/ext-tmpl-2e746d706c/hello.tmpl) creato, verifiche pendenti |
| `.tpl` | [hello.tpl](variants/ext-tpl-2e74706c/hello.tpl) creato, verifiche pendenti |
