require "erb"

audience = "World"
rendered = ERB.new(File.read("hello.erb", encoding: "UTF-8")).result(binding)
raise "Unexpected rendering" unless rendered == "<p>Hello, World!</p>\n"
print rendered
