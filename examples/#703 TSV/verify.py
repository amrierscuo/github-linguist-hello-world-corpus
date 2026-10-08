import csv
with open("hello.tsv", encoding="utf8", newline="") as stream:
    rows = list(csv.DictReader(stream, delimiter="\t"))
assert len(rows) == 1 and rows[0] == {"key":"greeting", "value":"Hello, World!"}
print(rows[0]["value"])
