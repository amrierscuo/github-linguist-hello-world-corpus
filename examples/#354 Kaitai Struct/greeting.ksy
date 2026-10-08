meta:
  id: greeting
  endian: le
seq:
  - id: magic
    contents: [0x48, 0x57]
  - id: length
    type: u1
  - id: message
    type: str
    size: length
    encoding: UTF-8
