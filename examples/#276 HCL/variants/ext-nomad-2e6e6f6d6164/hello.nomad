job "corpus-greeting" {
  datacenters = ["dc1"]
  type = "batch"
  group "hello" {
    task "greet" {
      driver = "raw_exec"
      config {
        command = "/usr/bin/printf"
        args = ["Hello, World!\n"]
      }
    }
  }
}
