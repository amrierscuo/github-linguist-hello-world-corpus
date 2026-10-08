from pathlib import Path
from email import policy
from email.parser import BytesParser
raw = Path(__file__).with_name('hello.eml').read_bytes()
message = BytesParser(policy=policy.default).parsebytes(raw)
assert not message.defects, message.defects
assert str(message['Subject']) == 'Hello, World!'
assert message['From'].addresses[0].addr_spec == 'sender@example.invalid'
assert message['To'].addresses[0].addr_spec == 'recipient@example.invalid'
assert message.get_content_type() == 'text/plain'
assert message.get_content_charset() == 'utf-8'
assert message.get_content() == 'Hello, World!\r\n'
serialized = message.as_bytes(policy=policy.SMTP)
reloaded = BytesParser(policy=policy.default).parsebytes(serialized)
assert reloaded.get_content() == message.get_content()
print('Hello, World!')
print('Python RFC 5322/MIME message parse, headers and content roundtrip PASS; no message sent.')
