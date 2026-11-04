from importlib.util import spec_from_file_location, module_from_spec
from importlib.machinery import SourceFileLoader
from io import BytesIO, StringIO
from wsgiref.handlers import SimpleHandler
from wsgiref.validate import validator
import sys
loader=SourceFileLoader("corpus_fixture",sys.argv[1])
spec=spec_from_file_location(loader.name,sys.argv[1],loader=loader)
module=module_from_spec(spec)
loader.exec_module(module)
stream=BytesIO(); errors=StringIO()
environ=dict(REQUEST_METHOD="GET",SCRIPT_NAME="",PATH_INFO="/",QUERY_STRING="",
 SERVER_NAME="localhost",SERVER_PORT="80",SERVER_PROTOCOL="HTTP/1.1",
 HTTP_HOST="localhost",CONTENT_LENGTH="",CONTENT_TYPE="")
handler=SimpleHandler(BytesIO(),stream,errors,environ,multithread=False,multiprocess=False)
handler.run(validator(module.application))
raw=stream.getvalue()
assert not errors.getvalue(),errors.getvalue()
head,body=raw.split(b"\r\n\r\n",1)
assert b"200 OK" in head.splitlines()[0],head
assert b"Content-Type: text/plain; charset=utf-8" in head.splitlines(),head
assert b"Content-Length: 14" in head.splitlines(),head
assert body==b"Hello, World!\n",body
print("PASS: native wsgiref handler returned exact status, headers and body")
print(body.decode("ascii"),end="")
