import system.io

def greeting : string := "Hello, " ++ "World!"
example : greeting.length = 13 := rfl

def main : io unit := io.put_str_ln greeting
