# 0174 E-mail — variante `.mbox`

Ruolo: Mailbox mbox con separatore From_ e un messaggio RFC 5322 originale, non soltanto un file EML rinominato.

Tipo variante: **adapted**. Modello di partenza: examples/#174 E-mail/hello.eml; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Python mailbox.mbox("hello.mbox"): leggere il messaggio, controllare Subject e body Hello, World!.
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.rfc-editor.org/rfc/rfc5322](https://www.rfc-editor.org/rfc/rfc5322)
- [https://docs.python.org/3/library/email.parser.html](https://docs.python.org/3/library/email.parser.html)
- [https://docs.python.org/3/library/email.policy.html](https://docs.python.org/3/library/email.policy.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.python.org/3/library/mailbox.html](https://docs.python.org/3/library/mailbox.html)
