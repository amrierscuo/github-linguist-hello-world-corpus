(defmodule hello (export (main 0)))

(defun main ()
  (io:format "Hello, ~s!~n" (list "World")))
