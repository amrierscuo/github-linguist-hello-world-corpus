# #193 Elvish Transcript

Rappresentare una sessione Elvish Transcript con un comando echo e il suo risultato atteso.

Tipo canonico `programming`, language_id `452025714`.

Toolchain prevista: Parser originale Go src.elv.sh/pkg/transcript e runtime Elvish 0.21.0.

Dalla cartella dell’esempio:

```sh
go mod tidy
go run verify.go [percorso del binario elvish]
```

Risultato atteso: una interazione, codice echo del saluto e output `Hello, World!` seguito da LF.

Il riferimento canonico non elenca estensioni per questa voce; .elvts è l’estensione del formato nei manuali originali. Un transcript non va passato direttamente all’interprete come se fosse un normale .elv.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Go 1.27.1 + src.elv.sh/pkg/transcript v0.21.0 + Elvish 0.21.0. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [Elvish — formato transcript e parser](https://pkg.go.dev/src.elv.sh/pkg/transcript)
- [Elvish — test transcript originali](https://github.com/elves/elvish/blob/main/docs/testing.md)
