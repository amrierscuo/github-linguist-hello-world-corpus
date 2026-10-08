Red/System [Title: "Corpus Greeting"]
#import [
    "libc.so.6" cdecl [
        puts: "puts" [message [c-string!] return: [integer!]]
    ]
]
puts "Hello, World!"
