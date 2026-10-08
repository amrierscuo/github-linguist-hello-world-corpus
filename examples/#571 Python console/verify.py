import doctest
result=doctest.testfile("hello.pycon",module_relative=False,verbose=True)
assert result.failed==0 and result.attempted==2
