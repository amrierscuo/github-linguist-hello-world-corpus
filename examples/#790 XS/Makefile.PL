use ExtUtils::MakeMaker;
WriteMakefile(NAME => 'Corpus::Greeting', VERSION_FROM => 'lib/Corpus/Greeting.pm', XS => {'Greeting.xs' => 'Greeting.c'});
