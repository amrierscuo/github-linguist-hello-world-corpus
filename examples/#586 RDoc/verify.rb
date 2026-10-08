require "rdoc"
require "rdoc/markup"
require "rdoc/markup/to_html"
source = File.read("hello.rdoc")
html = RDoc::Markup.parse(source).accept(RDoc::Markup::ToHtml.new(RDoc::Options.new))
raise "missing greeting" unless html.include?("Hello, World!") && html.include?("<h1")
puts "Hello, World!"
