# #011 AMPL

`hello.ampl` usa il comando AMPL `printf` per emettere `Hello, World!` seguito
da un ritorno a capo. Non richiede un modello, un solver o un problema di ottimizzazione.

## Toolchain e comando

Serve l'interprete ufficiale AMPL. Dalla cartella dell'esempio, con `ampl` nel PATH:

```powershell
ampl hello.ampl
```

Risultato atteso su stdout: una sola riga `Hello, World!`, codice di uscita 0.

## Verifica eseguita

Sintassi e semantica verificate su Windows con AMPL Version 20260809, proveniente
dal pacchetto ufficiale `ampl_module_base-20260809-py3-none-win_amd64.whl`.
La distribuzione contiene una licenza demo sufficiente a eseguire questo comando;
non è stata attivata una licenza personale. Sono stati verificati il codice
di uscita, l'assenza di stderr e i byte di stdout: `b'Hello, World!\r\n'` su
Windows. Il checker ammette un solo terminatore LF oppure CRLF; non ammette
testo aggiuntivo. Vedere `verification.log`.

Per riprodurre il controllo con l'interprete installato o estratto localmente:

```powershell
python verify.py --ampl /percorso/di/ampl.exe
```

`verify.py` avvia l'interprete reale e confronta il risultato; non interpreta AMPL.
Il binario e la licenza non fanno parte del corpus. Il log registra origine e SHA-256
della distribuzione usata; le disponibilità future delle licenze seguono AMPL.

## Fonti primarie

- [AMPL: capitolo ufficiale sui comandi di output, sezione printf](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf)
- [AMPL: integrazione Python e distribuzione moduli](https://dev.ampl.com/ampl/python/index.html)
- [Indice ufficiale del modulo AMPL base](https://pypi.ampl.com/ampl-module-base/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ampl` | [hello.ampl](hello.ampl) verificato |
| `.mod` | [hello.mod](variants/ext-mod-2e6d6f64/hello.mod) creato, verifiche pendenti |
