module Audience where
import {-# SOURCE #-} Greeting (greeting)
audience :: String
audience = "World"
keepGreeting :: String
keepGreeting = greeting
