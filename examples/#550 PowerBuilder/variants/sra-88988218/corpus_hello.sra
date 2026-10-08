$PBExportHeader$corpus_hello.sra
forward
global type corpus_hello from application
end type
end forward

global type corpus_hello from application
string appname = "Corpus greeting"
end type
global corpus_hello corpus_hello

event open;
MessageBox("Corpus greeting", "Hello, World!")
end event
