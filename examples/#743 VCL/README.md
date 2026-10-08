# #743 VCL

Interpretare Varnish VCL e rispondere con una pagina sintetica di saluto.

Tipo canonico `programming`, language_id `384`.

Toolchain prevista: Varnish varnishd.

Dalla cartella dell’esempio:

```sh
varnishd -C -f hello.vcl; avviare una istanza isolata su loopback e richiederne la risposta.
```

Risultato atteso: VCL accettato; HTTP200 body Hello, World! e newline.

La risposta è sintetica: non usa il backend o la rete esterna.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Varnish VCL](https://varnish-cache.org/docs/trunk/reference/vcl.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vcl` | [hello.vcl](hello.vcl) creato, verifiche pendenti |
