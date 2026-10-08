require 'erb'
audience = 'World'
actual = ERB.new(File.read('hello.axs.erb')).result(binding)
raise 'Unexpected rendering' unless actual.include?(%q{SEND_STRING 0,"'Hello, World!'"})
print actual
