GET http://127.0.0.1:{{port}}/greeting

HTTP 200
[Asserts]
body == "Hello, World!"
