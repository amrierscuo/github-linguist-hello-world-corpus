gem "haml", "= 6.3.0"
require "haml"

source = File.read("hello.haml", encoding: "UTF-8")
rendered = Haml::Template.new { source }.render
raise "Unexpected rendering" unless rendered.strip == "<p>Hello, World!</p>"
print rendered
