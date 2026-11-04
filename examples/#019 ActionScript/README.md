# #019 ActionScript

`HelloWorld.as` is a **ActionScript 3** document class derived from `Sprite`.
The manufacturer creates a `TextField`, assigns `Hello World` and adds it to the
View list. Greetings appear on stage, not in the console.

Required toolchain: compilatore `mxmlc` (Apache Flex SDK con la libreria
`playerglobal.swc` appropriate) and a SWF compatible runtime.
of the example, with the compiler configured in the PATH, this command compiles
e controlla la syntax ActionScript:

```sh
mxmlc -strict=true -output=HelloWorld.swf HelloWorld.as
```

Expected result of syntactic control: zero output code and creation
of `HelloWorld.swf` without errors. This command is recorded as both build
both as a voice verification command; it does not verify the rendering alone.

To control the behavior you need to open the file generated in a SWF runtime
compatible with ActionScript 3 and observe the `Hello World` text on the stage.
The precise command of execution depends on the chosen runtime; this part
resta da fissare e verificare.

syntax and behavior verified: **no**. Blocchi attuali: compilatore Flex,
`playerglobal.swc` and SWF runtime not available in the environment used.
text of the source does not replace compilation and execution.

Riferimenti primari: [compilatori Flex, Apache](https://flex.apache.org/doc/flex/using/flx_mxml_mx.html)
e [TextField, Adobe](https://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.as` | [HelloWorld.as](HelloWorld.as) created; verification pending |
