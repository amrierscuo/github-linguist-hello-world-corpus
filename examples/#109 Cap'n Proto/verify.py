from pathlib import Path
import capnp

schema = capnp.load(str(Path(__file__).with_name("hello.capnp")))
message = schema.Greeting.new_message()
assert message.message == "Hello, World!"
payload = message.to_bytes()
with schema.Greeting.from_bytes(payload) as restored:
    assert restored.message == "Hello, World!"
    print(restored.message)
