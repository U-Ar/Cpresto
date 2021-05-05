grammar Hello;

options { language=Python3; }

parse : 'hello' ID;
ID : [a-z]+ ;
WS : [ \t\r\n]+ -> skip ;