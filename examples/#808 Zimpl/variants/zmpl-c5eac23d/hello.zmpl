set I := {1..13};
param code[I] := <1> 72, <2> 101, <3> 108, <4> 108, <5> 111, <6> 44, <7> 32, <8> 87, <9> 111, <10> 114, <11> 108, <12> 100, <13> 33;
var x[I] real >= code[I] <= code[I]+1;
minimize greeting: sum <i> in I: x[i];
subto complete: sum <i> in I: x[i] >= 1129;
