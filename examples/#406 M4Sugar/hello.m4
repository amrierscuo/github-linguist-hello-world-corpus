m4_init
m4_divert_push([0])dnl
m4_define([greeting], [Hello, World!])dnl
greeting
m4_divert_pop([0])dnl
