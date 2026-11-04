# #193 Elvish Transcript

Represent an Elvish Transcript session with an echo command and its expected result.

Canonical type `programming`, language_id `452025714`.

Suggested toolchain: Parser original Go src.elv.sh / pkg/transcript and runtime Elvish 0.21.0.

From the example directory:

```sh
go mod tidy
go run verify.go [percorso del binario elvish]
```

Expected result: an interaction, echo code of greeting and `Hello, World!` output followed by LF.

The canonical reference does not list extensions for this item; .elvts is the extension of the format in the original manuals. A transcript should not be passed directly to the interpreter as if it were a normal .elv.

Recorded status: syntax verified; behavior verified. Toolchain: Go 1.27.1 + src.elv.sh/pkg/transcript v0.21.0 + Elvish 0.21.0. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [Elvish — formato transcript e parser](https://pkg.go.dev/src.elv.sh/pkg/transcript)
- [Elvish — test transcript originali](https://github.com/elves/elvish/blob/main/docs/testing.md)
