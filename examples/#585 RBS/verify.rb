require "rbs"
parsed = RBS::Parser.parse_signature(File.read("hello.rbs"))
declarations = parsed.last.is_a?(Array) ? parsed.last : parsed
entry = declarations.find { |item| item.is_a?(RBS::AST::Declarations::Alias) }
raise "missing greeting alias" unless entry && entry.name.to_s.end_with?("greeting")
raise "wrong literal" unless entry.type.literal == "Hello, World!"
puts entry.type.literal
