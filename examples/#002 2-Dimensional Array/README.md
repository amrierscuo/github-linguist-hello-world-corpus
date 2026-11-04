# #002 2-Dimensional Array

`hello.2da` is a **2DA V1.0** table, a variant used by the Infinity Engine.
`0` line contains `Hello,` in `GREETING` column and `World!` in column
`TARGET`. It is an example of data, so it does not print a message independently.
Reading the two values and separating them with a space you get `Hello, World!`.

Header identifies format; the second row `****` is the value
default. In this variant the values are separated by spaces and cannot
contain a space within them: for this reason the greeting uses two cells.

## Toolchain and reproducible verification

The planned verification path is the native 2DA importer of **GemRB**, via
its Python console, with the file available between the resources of the game as
`hello.2da`:

```python
import GemRB
from GUIDefines import GTV_STR
t = GemRB.LoadTable("hello")
greeting = t.GetValue(0, 0, GTV_STR) + " " + t.GetValue(0, 1, GTV_STR)
assert greeting == "Hello, World!"
```

There is no step in compiling the data file. Import must succeed,
with a row and two columns, and the arrangement must pass.
with risorse/configurazione game. The file does not replace tables of the game:
has a dedicated name.

## Status and limitations

Artefatto created; syntax e behavior **non ancora verificate da un lettore 2DA**.
GemRB and a gaming environment are not available in this session. La
visual correspondence with the specification is not counted as validation.

## Primary sources

- [IESDP, specifica di 2DA V1.0](https://gibberlings3.github.io/iesdp/file_formats/ie_formats/2da.htm).
- [GemRB, implementazione dell'importatore 2DA](https://github.com/gemrb/gemrb/blob/master/gemrb/plugins/2DAImporter/2DAImporter.cpp).
- [GemRB, caricamento dei dati tabellari](https://gemrb.org/GUIScript/functions/LoadTable.html).
- [GemRB, lettura delle celle e tipo `GTV_STR`](https://gemrb.org/GUIScript/functions/Table_GetValue.html).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.2da` | [hello.2da](hello.2da) created; verification pending |
