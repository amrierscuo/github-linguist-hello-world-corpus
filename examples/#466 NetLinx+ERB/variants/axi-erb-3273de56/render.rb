require "erb"
audience = "World"
File.write("hello.axi", ERB.new(File.read("hello.axi.erb")).result(binding))
