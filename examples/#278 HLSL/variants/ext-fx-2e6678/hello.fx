float4 GreetingPixel(float4 position : SV_Position) : SV_Target {
 static const float text[13] = {72,101,108,108,111,44,32,87,111,114,108,100,33};
 int i = clamp((int)position.x, 0, 12);
 return float4(text[i]/255.0, text[i]/255.0, text[i]/255.0, 1.0);
}
technique10 CorpusGreeting {
 pass GreetingPass {
  SetPixelShader(CompileShader(ps_4_0, GreetingPixel()));
 }
}
