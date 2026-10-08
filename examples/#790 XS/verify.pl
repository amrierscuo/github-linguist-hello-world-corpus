use strict;
use warnings;
use blib;
use Corpus::Greeting;
my $actual = Corpus::Greeting::greeting();
die "Unexpected XS value" unless $actual eq 'Hello, World!';
print "$actual\n";
