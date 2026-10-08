from setuptools import Extension, setup
from Cython.Build import cythonize
setup(name="corpus_cython_greeting", ext_modules=cythonize([Extension("hello", ["hello.pyx"])], language_level=3))
