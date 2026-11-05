define program
    [repeat token]
end define

function main
    replace [program]
        Input [repeat token]
    construct Greeting [program]
        "Hello, World!"
    by
        Greeting
end function
