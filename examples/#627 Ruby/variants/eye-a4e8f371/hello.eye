Eye.application "corpus-greeting" do
  working_dir File.dirname(__FILE__)
  process "greeting" do
    pid_file "greeting.pid"
    start_command "ruby greeting.rb"
    daemonize true
    auto_start false
  end
end
