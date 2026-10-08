God.watch do |w|
  w.name = "corpus-greeting"
  w.start = "ruby " + File.join(File.dirname(__FILE__), "greeting.rb")
  w.pid_file = File.join(File.dirname(__FILE__), "greeting.pid")
  w.keepalive
end
