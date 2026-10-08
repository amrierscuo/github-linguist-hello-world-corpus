# #181 Earthly

Eseguire un target Earthly che produce un file contenente Hello, World! seguito da LF.

Tipo canonico `programming`, language_id `963512632`.

Toolchain prevista: Earthly 0.8+ con backend BuildKit e ambiente per immagini Linux.

Dalla cartella dell’esempio:

```sh
earthly +greeting
```

Risultato atteso: artefatto locale greeting.txt, esattamente 14 byte `Hello, World!\n`.

Il target salva soltanto un artefatto locale. L’immagine Alpine è fissata alla serie 3.20; riproduzione stretta richiede anche il digest dell’immagine. Il backend container non è stato predisposto.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [Earthfile reference](https://docs.earthly.dev/docs/earthfile)
