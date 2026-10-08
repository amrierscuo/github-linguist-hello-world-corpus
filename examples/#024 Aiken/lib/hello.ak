pub fn greeting() -> ByteArray {
  "Hello, World!"
}

test greeting_has_exact_bytes() {
  greeting() == #[72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
}

test greeting_rejects_other_text() {
  greeting() != "Goodbye, World!"
}
