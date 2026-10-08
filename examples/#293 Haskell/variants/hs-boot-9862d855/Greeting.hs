module Greeting where
import Audience (audience)
greeting :: String
greeting = "Hello, " ++ audience ++ "!"
