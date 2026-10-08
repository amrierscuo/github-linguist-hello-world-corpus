Shader "Corpus/Hello World" {
 Properties { _Color ("Hello, World!", Color) = (0.1,0.3,0.5,1) }
 SubShader { Pass { Color [_Color] } }
 Fallback Off
}
