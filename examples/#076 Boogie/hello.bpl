// The result is the 13 ASCII code points of Hello, World!.
procedure Greeting() returns (length: int, message: [int]int);
  ensures length == 13;
  ensures message[0] == 72 && message[1] == 101 && message[2] == 108 && message[3] == 108 && message[4] == 111 && message[5] == 44 && message[6] == 32 && message[7] == 87 && message[8] == 111 && message[9] == 114 && message[10] == 108 && message[11] == 100 && message[12] == 33;

implementation Greeting() returns (length: int, message: [int]int)
{
  length := 13;
  message[0] := 72;
  message[1] := 101;
  message[2] := 108;
  message[3] := 108;
  message[4] := 111;
  message[5] := 44;
  message[6] := 32;
  message[7] := 87;
  message[8] := 111;
  message[9] := 114;
  message[10] := 108;
  message[11] := 100;
  message[12] := 33;
}
