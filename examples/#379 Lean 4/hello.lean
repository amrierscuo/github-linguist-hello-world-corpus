def greeting : String := "Hello, " ++ "World!"
theorem greeting_length : greeting.length = 13 := by decide

def main : IO Unit := IO.println greeting
