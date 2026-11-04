# #438 Modelica

Simulate a Model model that prints greeting in the initial algorithm.

Canonical type `programming`, language_id `233`.

Suggested toolchain: OpenModelica omc and Standard Library Model.

From the example directory:

```sh
omc run.mos
```

Expected result: loaded and simulated model; stdout/log contains Hello, World!.

Streams.print is performed during initialization. The model does not change external devices.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Modelica — linguaggio e specifica](https://specification.modelica.org/maint/3.6/)
- [OpenModelica — scripting](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/scripting_api.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mo` | [Hello.mo](Hello.mo) created; verification pending |
