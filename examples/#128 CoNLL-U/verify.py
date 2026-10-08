from pathlib import Path
import sys
from conllu import parse

sentences = parse(Path(sys.argv[1]).read_text(encoding="utf-8"))
assert len(sentences) == 1
sentence = sentences[0]
text = "".join(token["form"] + ("" if (token["misc"] or {}).get("SpaceAfter") == "No" else " ")
               for token in sentence if isinstance(token["id"], int)).rstrip()
assert text == sentence.metadata["text"] == "Hello, World!", text
assert [token["id"] for token in sentence if token["head"] == 0] == [1]
assert sentence[2]["head"] == 1 and sentence[2]["deprel"] == "vocative"
print(text)
print("PASS: existing conllu parser; detokenization and declared dependency example")
