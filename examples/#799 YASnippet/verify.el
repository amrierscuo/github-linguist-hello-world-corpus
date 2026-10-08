;;; verify.el --- Verify snippet parsing and expansion -*- lexical-binding: t; -*-
(require 'cl-lib)
(require 'yasnippet)

(with-temp-buffer
  (setq buffer-file-name (expand-file-name "hello.yasnippet"))
  (insert-file-contents buffer-file-name)
  (snippet-mode)
  (let ((definition (yas--parse-template buffer-file-name)))
    (cl-assert (equal (nth 0 definition) "greeting"))
    (cl-assert (equal (nth 2 definition) "Corpus greeting")))
  (yas-load-snippet-buffer 'text-mode))

(with-temp-buffer
  (text-mode)
  (yas-minor-mode 1)
  (insert "greeting")
  (cl-assert (yas-expand))
  (cl-assert (equal (buffer-string) "Hello, World!\n"))
  (let* ((snippet (car (yas-active-snippets t)))
         (field (cl-find 1 (yas--snippet-fields snippet)
                         :key #'yas--field-number)))
    (cl-assert field)
    (cl-assert (equal (buffer-substring-no-properties
                      (yas--field-start field) (yas--field-end field)) "World")))
  (princ (buffer-string))
  (princ "YASnippet parser, trigger and placeholder PASS\n"))
