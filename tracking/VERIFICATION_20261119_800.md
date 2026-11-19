# Verification of 800 main examples on November 19, 2026

This batch recorded 6 new behavior checks. The corpus contains 800 main examples with verified syntax and 800 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_794.md) records the earlier checks in this session.

- **#183 Ecere Projects**. The publisher project generator loaded the exact .epj and its source. The native Windows console executable emitted the exact greeting. The same evidence covers `.epj`. [Evidence](../examples/%23183%20Ecere%20Projects/verification/native_20261119_wave800_main.json).
- **#238 Genero per**. The compatible form compiler accepted the recorded legacy SCREEN specification. The static label positions in its compiled XML reconstruct the exact greeting, with no graphical front end. The same evidence covers `.per`. [Evidence](../examples/%23238%20Genero%20per/verification/native_20261119_wave800_main.json).
- **#477 Nu**. The unchanged Nu program ran in the publisher runtime. Its actual puts operation emitted the exact greeting. The same evidence covers `.nu`. [Evidence](../examples/%23477%20Nu/verification/native_20261119_wave800_main.json).
- **#503 OpenEdge ABL**. FWD converted the unchanged ABL program. The generated source and compiled JVM instructions bind the exact greeting to the informational message operation with its OK button. The check inspects compiled behavior and opens no dialog. [Evidence](../examples/%23503%20OpenEdge%20ABL/verification/native_20261119_wave800_main.json).
- **#726 Turing**. The compatible publisher compiler accepted the unchanged Turing program and its generated native executable emitted the exact greeting. The same evidence covers `.t`. [Evidence](../examples/%23726%20Turing/verification/native_20261119_wave800_main.json).
- **#814 eC**. The publisher compiler compiled the unchanged eC program using a disposable project fixture. The native Windows console executable emitted the exact greeting. The same evidence covers `.ec`. [Evidence](../examples/%23814%20eC/verification/native_20261119_wave800_main.json).

941 of 1,749 language and extension pairs now have verified behavior.
