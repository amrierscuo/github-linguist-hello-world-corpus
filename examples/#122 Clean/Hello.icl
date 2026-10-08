module Hello
import StdEnv

Start :: *World -> *World
Start world
    # (console, world) = stdio world
    # console = fwrites ("Hello, " +++ "World!\n") console
    # (_, world) = fclose console world
    = world
