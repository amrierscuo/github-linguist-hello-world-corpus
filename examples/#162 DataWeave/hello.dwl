%dw 2.0
output application/json
var target = "World"
---
{ greeting: "Hello, " ++ target ++ "!" }
