from pathlib import Path
from pygments.lexers.special import RawTokenLexer
from pygments.token import Token
value = list(RawTokenLexer().get_tokens_unprocessed(Path("hello.raw").read_text(encoding="utf-8")))
assert value == [(0, Token.Literal.String, "Hello, World!")]
print(value[0][2])
