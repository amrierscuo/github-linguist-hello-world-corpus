require "thor"
class CorpusGreeting < Thor
  desc "hello", "Print original greeting"
  def hello
    puts "Hello, World!"
  end
end
CorpusGreeting.start(ARGV)
