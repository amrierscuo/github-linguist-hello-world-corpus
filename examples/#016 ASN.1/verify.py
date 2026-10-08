"""Parse the ASN.1 module and round-trip its declared greeting using DER."""
from pathlib import Path
import platform
import asn1tools

source = Path(__file__).with_name("hello.asn")
parsed = asn1tools.parse_files(str(source))
greeting = parsed["HelloWorld"]["values"]["hello"]["value"]
codec = asn1tools.compile_files(str(source), codec="der")
encoded = codec.encode("Greeting", greeting, check_constraints=True)
decoded = codec.decode("Greeting", encoded, check_constraints=True)
if greeting != "Hello World" or decoded != greeting:
    raise SystemExit("FAIL: greeting round-trip differs from Hello World")
if encoded.hex() != "0c0b48656c6c6f20576f726c64":
    raise SystemExit("FAIL: unexpected DER bytes")
print(f"Python: {platform.python_version()}")
print(f"asn1tools: {asn1tools.__version__}")
print("ASN.1 module: HelloWorld; type: Greeting; value: hello")
print(f"DER: {encoded.hex()}")
print(f"Decoded: {decoded}")
print("PASS: parse, compile, encode and decode")
