static const float corpus_text[13] = {72,101,108,108,111,44,32,87,111,114,108,100,33};
float corpusGreetingValue(int i) { return corpus_text[clamp(i,0,12)] / 255.0; }
