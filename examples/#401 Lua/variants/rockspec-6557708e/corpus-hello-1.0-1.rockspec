rockspec_format = "3.0"
package = "corpus-hello"
version = "1.0-1"
source = { url = "file://./corpus-hello-1.0.tar.gz" }
description = { summary = "Hello, World!", license = "MIT" }
build = { type = "builtin", modules = { corpus_hello = "corpus_hello.lua" } }
