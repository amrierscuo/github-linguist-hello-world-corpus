module 0x42::greeting {
    use std::string::{Self, String};

    public fun hello(): String {
        string::utf8(b"Hello, World!")
    }

    #[test]
    fun greeting_is_exact() {
        assert!(hello() == string::utf8(b"Hello, World!"), 0);
    }
}
