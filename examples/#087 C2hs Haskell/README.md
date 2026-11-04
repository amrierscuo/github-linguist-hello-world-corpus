# #087 C2hs Haskell

Solve with C2HS the constant C HELLO_SENTINEL = 1 and print Hello, World! from the Haskell program generated when the value is correct.

## Reproduction

Toolchain: C2HS 0.28.8; GHC 9.4.7. Test environment: Ubuntu 24.04 WSL2 x86_64.

```text
mkdir -p build
c2hs --cppopts=-I. Hello.chs -o build/Hello.hs
ghc build/Hello.hs -o build/hello
./build/hello
```

Expected result: C2HS generates Haskell with constant 1; GHC compile; Hello, World! print runtime, exit 0.

## Verification

syntax and behavior verified 2026-10-08T23:34:12.651012+00:00. The variants have separate evidence in the log when consumed.

[Prova nativa](verification/finish_native.json) contains versions, real commands, exit code, output and SHA-256. The local routes are replaced by placeholders.

## Primary sources

- [https://github.com/haskell/c2hs](https://github.com/haskell/c2hs)
- [https://github.com/haskell/c2hs/wiki/User-Guide](https://github.com/haskell/c2hs/wiki/User-Guide)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.chs` | [Hello.chs](Hello.chs) syntax and behavior verified |
