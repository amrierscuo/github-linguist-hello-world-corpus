shader_type canvas_item;
#include "res://hello.gdshaderinc"
void fragment() { COLOR = vec4(corpus_greeting_color(UV.x), 1.0); }
