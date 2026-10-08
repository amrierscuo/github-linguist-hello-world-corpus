# 0730 — TypeScript — `.mts`

Modulo TypeScript ECMAScript determinato dal suffisso.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.mts`.

Controllo previsto, dalla cartella della variante:

```text
tsc --target ES2022 --module NodeNext --moduleResolution NodeNext --outDir work hello.mts; node work/hello.mjs
```

Risultato atteso: Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.typescriptlang.org/docs/handbook/modules/reference.html#module-format-detection](https://www.typescriptlang.org/docs/handbook/modules/reference.html#module-format-detection)
