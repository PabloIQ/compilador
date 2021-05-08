#-----------------Analizador para PL0
#El uso más común para re es buscar patrones en texto. La función search() toma el patrón y el texto para escanear,
#y devuelve un objeto Match cuando se encuentra el patrón. Si el patrón no se encuentra, search() devuelve None .

import analizador_lexico.ply.lex as lex
import re
import codecs

constant = ('NUMBER','ID')
operadorAritmet = ('PLUS',
                     'MINUS',
                     'MULTI',
                     'DIVIDE')
operadorRelacional = ('ODD',
                          'EQUAL',
                          'NE',
                          'LT',
                          'LTE',
                          'GT',
                          'GTE')
delimitador = ('LPARENT',
                 'RPARENT',
                 'COMMA',
                 'SEMICOLOM',
                 'DOT',
                 'UPDATE')
reservadas = ('BEGIN',
              'END',
              'IF',
              'THEN',
              'WHILE',
              'DO',
              'CALL',
              'CONST',
              'INT',
              'PROCEDURE',
              'OUT',
              'IN',
              'ELSE')

tokens = (list(constant) + list(operadorAritmet) +
          list(operadorRelacional) + list(delimitador) +
          list(reservadas))
# DEFINICION DE LOS TOKENS DE EXPRESION REGULAR
# r'', define una expresion regular

#operadores
t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_MULTI     = r'\*'
t_DIVIDE    = r'/'
t_ODD       = r'ODD'
t_EQUAL    = r'='
t_NE        = r'<>'
t_LT        = r'<'
t_LTE       = r'<='
t_GT        = r'>'
t_GTE       = r'>='
#delimitadores
t_LPARENT   = r'\('
t_RPARENT   = r'\)'
t_COMMA     = r','
t_SEMICOLOM = r';'
t_DOT       = r'\.'
t_UPDATE    = r':='

# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"

#FUNCIONES 
#reconocimiento de identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #reconocer 'empiezar por' 'continua por' cerradura de cleen*
    if t.value.upper() in tokens:
        t.value = t.value.upper()
        t.type = t.value

    return t

#Regla para atrapar los saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#funcion para reconocer los comentarios
#no retorna nada despues del #
def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+' 
    #conincide con cualquier digito decimal
    #+ una o mas veces otro decimal
    t.value = int(t.value)
    return t

def t_error(t):
    #print("Caracter no valido '%s'" % t.value[0])
    t.lexer.skip(1)
    t.value = t.value[0]
    return t



def analisar(cadena=""):
    #Construyendo el lexer 
    analizador = lex.lex()
    analizador.input(cadena)

    #diccionario a retornar
    tokensFindedList = []
    #extrayendo tokens 'Tokenize'
    while True:
        tok = analizador.token()
        if not tok:
            break #fin del ciclo, ya no hay mas entradas
        
        varName = ""
        if tok.type in constant:
            if tok.type == "ID":
                varName = "Variable"
            else:
                varName = "Constante"
        elif tok.type in operadorAritmet:
            varName = "Operador Aritmético"
        elif tok.type in operadorRelacional:
            varName = "Operador Relacional"
        elif tok.type in delimitador:
            varName = "Delimitador"
        elif tok.type in reservadas:
            varName = "Palabra reservada"
        else:
            varName = "Caracter Inválido!"

        tokensFindedList.append([tok.type,tok.value,varName,tok.lineno])
        #print("tok.type   = ",tok.type,"tok.value = ",tok.value)
        #print("tok.lineno = ",tok.lineno,"tok.lexpos = ",tok.lexpos)

    return tokensFindedList