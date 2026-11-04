# #188 Edje Data Collection

Fill out a Edje group with a textual part showing Hello, World!.

Canonical type `data`, language_id `342840478`.

Toolchain provided: EFL/Edje with edje_cc and viewer edje_player or Edje application.

From the example directory:

```sh
edje_cc hello.edc hello.edj
edje_player hello.edj -g greeting
```

Expected result: greeting collection compiled; in the label part appears Hello, World!.

The compilation of the collection and the observation of the text in the viewer are distinct controls; it serves a EFL graphic environment with Sans font available.

Initial state: created; syntax and behavioral verification pending. native toolchain not yet performed: syntax and behavior verifications remain pending.

Sources of linguaggio/formato and original implementations:

- [Edje — riferimento EDC originale](https://github.com/Enlightenment/efl/blob/master/doc/edcref.dox)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.edc` | [hello.edc](hello.edc) created; verification pending |
