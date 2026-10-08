require '_h2ph_pre.ph';
no warnings qw(redefine misc);
unless (defined &CORPUS_GREETING) {
  sub CORPUS_GREETING () { "Hello, World!" }
}
1;
