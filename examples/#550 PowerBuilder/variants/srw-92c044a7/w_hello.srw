$PBExportHeader$w_hello.srw
forward
global type w_hello from window
end type
end forward

global type w_hello from window
integer width = 1600
integer height = 600
boolean titlebar = true
string title = "Hello, World!"
end type
global w_hello w_hello

event open;
MessageBox("Corpus greeting", "Hello, World!")
end event
