;;; verify.el --- Verify the original SRecode template -*- lexical-binding: t; -*-
(require 'cl-lib)
(require 'subr-x)
(require 'semantic)
(require 'srecode/compile)
(require 'srecode/insert)

(semantic-mode 1)
(srecode-compile-file (expand-file-name "hello.srt"))
(with-temp-buffer
  (text-mode)
  (srecode-insert "file:greeting")
  (cl-assert (string= (string-trim-right (buffer-string)) "Hello, World!"))
  (princ (buffer-string))
  (princ "\nSRecode parse and expansion PASS\n"))
