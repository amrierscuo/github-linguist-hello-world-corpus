actor Greeting {
  public query func hello(name : Text) : async Text {
    "Hello, " # name # "!"
  };
};
assert (await Greeting.hello("Reader")) == "Hello, Reader!";
await Greeting.hello("World");
