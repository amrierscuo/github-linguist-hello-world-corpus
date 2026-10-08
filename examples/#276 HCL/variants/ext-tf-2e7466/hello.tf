locals {
  greeting = "Hello, World!"
}
output "message" {
  value = local.greeting
}
