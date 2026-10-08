require "erb"
require "open3"
greeting = "Hello, World!"
source = ERB.new(File.read("hello.js.erb")).result(binding)
stdout, stderr, status = Open3.capture3([ENV.fetch("NODE_BINARY", "node"), "node"], stdin_data: source)
raise stderr unless status.success?
raise "unexpected stdout" unless stdout == "Hello, World!\n"
print stdout
