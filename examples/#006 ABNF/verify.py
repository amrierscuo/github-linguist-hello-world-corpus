"""Exercise the external abnf parser; this file does not implement ABNF parsing."""

from importlib.metadata import version
from pathlib import Path

from abnf import ParseError, Rule


class GreetingRule(Rule):
    pass


grammar = Path(__file__).with_name("hello.abnf").read_bytes().decode("ascii")
GreetingRule.load_grammar(grammar, strict=False)
rule = GreetingRule("greeting")
assert rule.parse_all("Hello, World!").value == "Hello, World!"
print(f"abnf {version('abnf')}: grammar parsed")
print("ACCEPT: Hello, World!")
for candidate in ("hello, World!", "Hello World!", "Hello, World! "):
    try:
        rule.parse_all(candidate)
    except ParseError:
        print(f"REJECT: {candidate!r}")
    else:
        raise AssertionError(f"Unexpected acceptance: {candidate!r}")
print("PASS: syntax and exact greeting semantics")
