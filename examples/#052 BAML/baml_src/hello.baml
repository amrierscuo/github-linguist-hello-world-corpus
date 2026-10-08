class Greeting {
  message "Hello, World!"
}

function Hello(name: string) -> Greeting {
  client "openai/gpt-4o-mini"
  prompt #"
    Return the exact greeting Hello, World! as the message field.
    This is a greeting for {{ name }}.
    {{ ctx.output_format }}
  "#
}

test GreetingForWorld {
  functions [Hello]
  args { name "World" }
}
