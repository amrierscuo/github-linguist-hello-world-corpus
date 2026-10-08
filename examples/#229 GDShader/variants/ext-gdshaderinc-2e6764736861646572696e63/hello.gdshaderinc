const int corpus_greeting[13] = {72,101,108,108,111,44,32,87,111,114,108,100,33};
vec3 corpus_greeting_color(float position) {
 int index = clamp(int(position * 13.0), 0, 12);
 return vec3(float(corpus_greeting[index]) / 255.0);
}
