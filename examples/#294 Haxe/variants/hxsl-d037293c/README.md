# 0294: Haxe: `.hxsl`

Role: Haxe class with shader HXSL Heaps real in SRC and constant greeting side host. The constant contains greeting; shader produces uniform color and does not draw letters.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Haxe4.3.3, pacchetto Ubuntu4.3.3-1build2. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
In una directory di lavoro copiare GreetingShader.hxsl come GreetingShader.hx; con Haxe + Heaps: haxe -lib heaps -main Main --interp. L’importer nativo del suffisso e il rendering GPU restano da verificare.
```

Risultato atteso: Il driver host stampa Hello, World!; il macro compiler HXSL analizza SRC. Non si promette testo renderizzato dallo shader.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- Heaps/HXSL not prepared with compatible version; macro compilation not performed.The historical frontend for the suffix .hxsl and the rendering GPU were not tested.

SHA-256 of variant files:

- `GreetingShader.hxsl`: `cd3ab7bf25278971b1e61638f3e594c2e953d5825cffc5ddd2315b9c84528e65`
- `Main.hx`: `6bfefc0879bc46a90004ae87b4398585e238e8ee49857ad5b461fe54f5c7db73`

Primary sources:

- https://heaps.io/documentation/hxsl.html
- https://raw.githubusercontent.com/pygments/pygments/master/pygments/lexers/haxe.py
- https://haxe.org/manual/introduction-hello-world.html
- https://api.haxe.org/Sys.html
