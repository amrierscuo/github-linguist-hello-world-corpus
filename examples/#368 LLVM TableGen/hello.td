class Greeting<string audience> {
  string Text = !strconcat("Hello, ", audience, "!");
}

def Hello : Greeting<"World">;
