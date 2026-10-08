program hello
  implicit none
  character(len=*), parameter :: target = 'World'
  print '(a)', 'Hello, ' // target // '!'
end program hello
