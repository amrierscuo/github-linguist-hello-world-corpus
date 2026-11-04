# #181 Earthly

Run a Earthly target that produces a Hello, World! file followed by LF.

Canonical type `programming`, language_id `963512632`.

Provided Toolchain: Earthly 0.8+ with BuildKit backend and Linux image environment.

From the example directory:

```sh
earthly +greeting
```

Expected result: local artifact greeting.txt, exactly 14 byte `Hello, World!\n`.

Il target salva soltanto un artefatto locale. L’immagine Alpine è fissata alla serie 3.20; riproduzione stretta richiede anche il digest dell’immagine. Il backend container non è stato predisposto.

Initial state: created; syntax and behavioral verification pending. native toolchain not yet performed: syntax and behavior verifications remain pending.

Sources of linguaggio/formato and original implementations:

- [Earthfile reference](https://docs.earthly.dev/docs/earthfile)
