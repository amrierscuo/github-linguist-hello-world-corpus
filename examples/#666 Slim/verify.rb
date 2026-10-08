require "slim"
result = Slim::Template.new("hello.slim").render
raise "unexpected output" unless result == "<p>Hello, World!</p>"
puts "Hello, World!"
