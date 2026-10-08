#!/usr/bin/env perl
use strict;
use warnings;
use FCGI;
while (FCGI::accept() >= 0) {
  print "Content-Type: text/plain\r\n\r\nHello, World!\n";
}
