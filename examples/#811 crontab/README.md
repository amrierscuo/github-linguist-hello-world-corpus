# #811 crontab

Analyze a crontab line and run only its command in the local fixture.

## Toolchain

CPython3.13.9; python-crontab3.4.0

## Procedure

pip install python-crontab; python verify.py

## Expected result

Schedule 0 9 * * * valida; comando emette Hello, World!.

## Status

syntax and behavior verified.

The existing parser reads time and command; the command is tried once. No cron is installed or planned.

Real check 2026-10-08T13:38:34.781824+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://man7.org/linux/man-pages/man5/crontab.5.html](https://man7.org/linux/man-pages/man5/crontab.5.html)
- [https://gitlab.com/doctormo/python-crontab](https://gitlab.com/doctormo/python-crontab)
