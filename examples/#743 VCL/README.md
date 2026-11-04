# #743 VCL

Native compilation and a loopback HTTP request confirmed status 200 and the exact greeting followed by a newline. The minimal correction uses a VCL long string to emit a real newline.

Canonical type: `programming`. Linguist language ID: `384`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with Varnish 7.1.1 in Ubuntu WSL2.

[Recorded commands, outputs and hashes](verification/native_20261104_vcl_candidate_receipt.json).
[Earlier check before the newline correction](verification/native_20261104_before_correction.json).

## Reproduce the check

Compile with `varnishd -C -f hello.vcl` and load the result in a disposable local Varnish instance. Request its loopback listener and compare the response body with Hello, World! followed by one LF. The receipt records the full startup and shutdown procedure.

## Primary sources


## Extension coverage

| Extension | Files | Status |
| --- | --- | --- |
| `.vcl` | [hello.vcl](hello.vcl) | Syntax and behavior verified |
