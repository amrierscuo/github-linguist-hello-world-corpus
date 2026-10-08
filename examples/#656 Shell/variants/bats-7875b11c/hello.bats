#!/usr/bin/env bats
@test "original greeting" {
  run printf "Hello, World!\n"
  [ "$status" -eq 0 ]
  [ "$output" = "Hello, World!" ]
}
