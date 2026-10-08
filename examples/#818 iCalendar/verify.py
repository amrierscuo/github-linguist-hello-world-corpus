from icalendar import Calendar
from pathlib import Path
c=Calendar.from_ical(Path("hello.ics").read_bytes())
events=c.walk("VEVENT")
assert len(events)==1
e=events[0]
assert str(e["SUMMARY"])=="Hello, World!"
assert e.decoded("DTEND")>e.decoded("DTSTART")
again=Calendar.from_ical(c.to_ical()).walk("VEVENT")[0]
assert str(again["SUMMARY"])=="Hello, World!"
print(str(e["SUMMARY"]))
