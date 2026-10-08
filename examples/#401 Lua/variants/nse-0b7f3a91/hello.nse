description = "Return a corpus greeting without network activity."
author = "Corpus Example"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = { "safe" }
prerule = function() return true end
action = function() return "Hello, World!" end
