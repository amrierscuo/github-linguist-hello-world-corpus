require "fcgi"
FCGI.each_cgi do |cgi|
  cgi.out("type" => "text/plain") { "Hello, World!\n" }
end
