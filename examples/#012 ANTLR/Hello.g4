grammar Hello;

message : 'Hello, World!' EOF;
WS : [ \t\r\n]+ -> skip;
