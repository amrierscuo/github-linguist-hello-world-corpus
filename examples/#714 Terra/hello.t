local C = terralib.includec("stdio.h")
terra main()
    C.puts("Hello, World!")
end
main()
