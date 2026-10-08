Pod::Spec.new do |s|
  s.name = "CorpusGreeting"
  s.version = "1.0.0"
  s.summary = "Hello, World!"
  s.homepage = "https://example.invalid/corpus-greeting"
  s.license = { :type => "MIT" }
  s.author = "Corpus Example"
  s.source = { :git => "https://example.invalid/corpus-greeting.git", :tag => s.version.to_s }
  s.source_files = "Greeting.h", "Greeting.m"
end
