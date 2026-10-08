(module
  (memory (export "memory") 1)
  (data (i32.const 0) "Hello, World!")
  (func (export "pointer") (result i32) i32.const 0)
  (func (export "length") (result i32) i32.const 13)
)
