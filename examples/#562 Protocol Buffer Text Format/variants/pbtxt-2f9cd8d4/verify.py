import pathlib,sys
sys.path.insert(0,sys.argv[1])
import hello_pb2
from google.protobuf import text_format
message=text_format.Parse(pathlib.Path("hello.pbtxt").read_text(),hello_pb2.Greeting())
encoded=message.SerializeToString()
decoded=hello_pb2.Greeting.FromString(encoded)
assert decoded.text=="Hello, World!"
print(decoded.text)
