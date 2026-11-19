Shader "Corpus/Hello World" {
 Properties { _Color ("Hello, World!", Color) = (0.1,0.3,0.5,1) }
 SubShader {
  Pass {
   HLSLPROGRAM
   #pragma vertex vert
   #pragma fragment frag

   float4 _Color;

   float4 vert(float4 position : POSITION) : SV_Position
   {
       return position;
   }

   float4 frag() : SV_Target
   {
       return _Color;
   }
   ENDHLSL
  }
 }
 Fallback Off
}
