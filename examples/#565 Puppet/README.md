# #565 Puppet

Apply a notify Puppet resource.

## Toolchain

Puppet

## Procedure

puppet parser validate hello.pp; puppet apply hello.pp

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Puppet parser/catalog/runtime Ruby non predisposti.

## Primary sources

- [https://www.puppet.com/docs/puppet/8/types/notify.html](https://www.puppet.com/docs/puppet/8/types/notify.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pp` | [hello.pp](hello.pp) created; verification pending |
