grammar Matrices;

programa
    : sentencia* EOF
    ;

sentencia
    : asignacion ';'
    | impresion ';'
    ;

asignacion
    : IDENTIFICADOR '=' expresion
    ;

impresion
    : 'imprimir' '(' IDENTIFICADOR ')'
    ;

expresion
    : matriz
    | IDENTIFICADOR
    | expresion '*' expresion
    ;

matriz
    : '[' filas ']'
    ;

filas
    : fila (',' fila)*
    ;

fila
    : '[' numeros ']'
    ;

numeros
    : NUMERO (',' NUMERO)*
    ;

// Reglas de tokens (lexer):

IDENTIFICADOR  
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

NUMERO         
    : [0-9]+ ('.' [0-9]+)?
    ;

WS  
    : [ \t\r\n]+ -> skip
    ;
