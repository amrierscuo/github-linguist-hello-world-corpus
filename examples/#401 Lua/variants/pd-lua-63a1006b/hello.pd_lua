local Greeting = pd.Class:new():register("hello")
function Greeting:initialize(sel, atoms)
  self.inlets = 1
  self.outlets = 1
  return true
end
function Greeting:in_1_bang()
  self:outlet(1, "symbol", { "Hello, World!" })
end
