# 0818: iCalendar: `.ical`

## Latest recorded verification

**Syntax and behavior verified** for `.ical`. icalendar: parse and serialize/reparse an event, preserve its summary and validate date ordering. [Recorded evidence](../../verification/native_20261104_followup_2e6963616c.json).

Textual variation of the same format, with canon suffix .ical.

Origin: copy of the original `examples/#818 iCalendar/hello.ics` file.

Artefatto principale: `hello.ical`.

Control provided, from the folder of the variant:

```text
Python icalendar: parse hello.ical; assert event SUMMARY
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.rfc-editor.org/rfc/rfc5545](https://www.rfc-editor.org/rfc/rfc5545)
- [https://icalendar.readthedocs.io/](https://icalendar.readthedocs.io/)
