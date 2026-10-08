#version 3.7;
global_settings { assumed_gamma 1.0 }
#declare Greeting = concat("Hello, ", "World!");
#debug concat(Greeting, "\n")
camera { location <0, 0, -3> look_at <0, 0, 0> }
background { color rgb <0.1, 0.2, 0.3> }
light_source { <-3, 4, -3> color rgb 1 }
sphere { <0, 0, 0>, 1 pigment { color rgb <0.8, 0.4, 0.1> } }
