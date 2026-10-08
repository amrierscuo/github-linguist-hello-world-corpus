use strict;
use warnings;
use Test::More tests => 1;
my $greeting = "Hello, " . "World!";
is($greeting, "Hello, World!", "corpus greeting");
