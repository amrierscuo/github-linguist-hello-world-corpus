# #662 Singularity

Costruire una container image da una definition Singularity e avviare il runscript.

Tipo canonico `programming`, language_id `987024632`.

Toolchain prevista: Apptainer o SingularityCE.

Dalla cartella dell’esempio:

```sh
apptainer build hello.sif Singularity
apptainer run hello.sif
```

Risultato atteso: runtime container stampa Hello, World! e newline.

La costruzione richiede l’immagine base e un runtime container; il file non viene contato come script shell puro.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Apptainer definition file](https://apptainer.org/docs/user/latest/definition_files.html)
