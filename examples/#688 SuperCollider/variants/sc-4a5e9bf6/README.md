# SuperCollider .sc

`hello.sc` contiene la classe `CorpusGreeting` con il metodo di classe `message`.

La classe è stata compilata nella SCClassLibrary isolata da sclang 3.13.0 e il metodo è stato eseguito tramite [run_class.scd](../../verification/run_class.scd). La post output contiene una riga esattamente `Hello, World!`; il processo termina con exit code 0.

La variante `.sc` non si esegue come un semplice script. La configurazione della class library e i comandi riproducibili sono descritti nel [README principale](../../README.md). Il [log](../../verification/resume_native.json) registra la compilazione di 330 file inclusa questa classe, l'invocazione effettiva, le versioni e lo SHA256 verificato.

Fonte primaria: [Writing Classes](https://doc.sccode.org/Guides/WritingClasses.html).
