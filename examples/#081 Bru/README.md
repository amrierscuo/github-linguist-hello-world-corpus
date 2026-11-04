# #081 Bru

Send a local GET request to hello.txt with Bruno and check in the request test that the answer contains Hello, World!.

## Toolchain

Node.js v22.20.0; @usebruno/lang 0.40.0; @usebruno/cli 4.2.1; Python stdlib HTTP fixture 3.13.9

## Commands and procedure

The commands must be run from the example folder. `npm install` installs
locally parser and CLI to the versions fixed in package.json. `node check.cjs`
attests the Bru file format. Start the fixture in a terminal:

```sh
python -m http.server 8765 --bind 127.0.0.1
```

Then, from another terminal in the same folder:

```sh
npx bru run hello.bru --noproxy --sandbox=safe
```

End the server when the test ends. The registered verification started
and automatically closed an equivalent fixture, and a request is executed
and the Bruno Real test. No external credentials or endpoints are required.

## Expected result

One GET request returned HTTP 200. The body was Hello, World! followed by a newline. The response greeting test passed with exit code 0.

## Status

syntax and behavior verified.

The server is a temporary fixture on loopback that serves hello.txt. The parser and the runner are the official Bruno ones. The node check.cjs command controls the format; the bru command also performs HTTP and test.

Actual verification of 2026-10-08T11:38:40.631298+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://docs.usebruno.com/bru-lang/overview](https://docs.usebruno.com/bru-lang/overview)
- [https://docs.usebruno.com/bru-cli/run/options](https://docs.usebruno.com/bru-cli/run/options)
- [https://github.com/usebruno/bruno](https://github.com/usebruno/bruno)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bru` | [hello.bru](hello.bru) verified |
