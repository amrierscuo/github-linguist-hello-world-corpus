module Main where

#include "hello.h"

main :: IO ()
main =
  if ({#const HELLO_SENTINEL #} :: Int) == 1
  then putStrLn "Hello, World!"
  else fail "Unexpected C constant"
