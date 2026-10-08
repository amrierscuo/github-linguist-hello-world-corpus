workflow "Greeting" {
  on = "push"
  resolves = ["greet"]
}
action "greet" {
  uses = "docker://alpine:3.20"
  args = ["/bin/echo", "Hello, World!"]
}
