define program
    [repeat token]
end define

function main
    replace [program]
        Input [repeat token]
    construct Greeting [stringlit]
        "Hello, World!"
    by
        Greeting
end function
