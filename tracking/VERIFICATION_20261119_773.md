# Verification of 773 main examples on November 19, 2026

This batch recorded 6 new behavior checks. The corpus contains 773 main examples with verified syntax and 773 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_767.md) records the earlier checks in this session.

- **#007 AGS Script**. The native AGS compiler compiled the room event with an explicit return type. The AGS disassembler confirmed that the event passes the exact greeting to its imported Display call. [Evidence](../examples/%23007%20AGS%20Script/verification/native_20261119_wave800_main.json).
- **#385 Limbo**. The compatible native Limbo compiler compiled the original module and the real Dis emulator invoked its init function, emitting the exact greeting. [Evidence](../examples/%23385%20Limbo/verification/native_20261119_wave800_main.json).
- **#525 Papyrus**. The compatible native compiler compiled the unchanged event. Decompilation of the actual PEX verified that OnInit passes the exact greeting to the native Debug.Trace call. The same evidence covers `.psc`. [Evidence](../examples/%23525%20Papyrus/verification/native_20261119_wave800_main.json).
- **#610 Redscript**. The actual compiler created a bundle from the original stand-alone function. The native decompiler read its compiled return instruction and recovered the exact greeting. Scope is the deterministic return value in emitted code. The same evidence covers `.reds`. [Evidence](../examples/%23610%20Redscript/verification/native_20261119_wave800_main.json).
- **#774 Witcher Script**. The compatible native AST parser recognized the unchanged, parameterless callable. The semantic probe resolved the single reachable return and evaluated its string literal against the declared type, yielding the exact greeting. The same evidence covers `.ws`. [Evidence](../examples/%23774%20Witcher%20Script/verification/native_20261119_wave800_main.json).
- **#787 XPages**. The harness resolved the original custom control from its XPages configuration. The real JSF Facelets renderer loaded the unchanged view and returned the greeting in the component’s HTML using the recorded XPages tag mapping. The same evidence covers `.xsp-config`. [Evidence](../examples/%23787%20XPages/verification/native_20261119_wave800_main.json).

918 of 1,749 language and extension pairs now have verified behavior.
