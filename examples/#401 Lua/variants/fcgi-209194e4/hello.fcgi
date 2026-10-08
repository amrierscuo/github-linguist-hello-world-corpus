#!/usr/bin/env lua
local fcgi = require("fcgi")
local request = fcgi.initRequest(0)
if request:accept() >= 0 then
  request:putStr("Content-Type: text/plain\r\n\r\nHello, World!\n")
  request:finish()
end
