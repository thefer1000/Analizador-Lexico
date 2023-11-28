import ply.yacc as yacc
from AnalizadorLéxico import tokens

# Gramática de Java básica
def p_program(p):
    '''program : class_declaration
               | program class_declaration'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_class_declaration(p):
    'class_declaration : CLASS ID LBRACE field_declaration RBRACE'
    p[0] = ('class_declaration', p[2], p[4])

def p_method_declaration(p):
    '''method_declaration : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ID RPAREN block'''
    p[0] = ('method_declaration', p[9], p[11])

def p_block(p):
    'block : LBRACE RBRACE'
    p[0] = ('block', [])

def p_field_declaration(p):
    '''field_declaration : type variable_declarator SEMICOLON
                        | field_declaration type variable_declarator SEMICOLON'''
    if len(p) == 4:
        p[0] = [('field_declaration', p[1], p[2])]
    else:
        p[0] = p[1] + [('field_declaration', p[2], p[3])]

def p_variable_declarator(p):
    '''variable_declarator : ID
                        | variable_declarator COMMA ID'''
    if len(p) == 2:
        p[0] = ('variable_declarator', p[1])
    else:
        p[0] = p[1] + ('variable_declarator', p[3])

def p_type(p):
    '''type : INT
            | FLOAT
            | DOUBLE
            | STRING
            | BOOLEAN'''
    p[0] = p[1]

# Construye el analizador sintáctico
parser = yacc.yacc()


# EJEMPLO DE RESPUESTA
#Tokens encontrados:
#('ID', 'public')
#('ID', 'class')
#('ID', 'Example')
#('ID', '{')
#('ID', 'public')
#('ID', 'static')
#('ID', 'void')
#('ID', 'main')
#('ID', '(')
#('ID', 'String')
#('ID', '[')
#('ID', ']')
#('ID', 'args')
#('ID', ')')
#('ID', '{')
#('ID', 'int')
#('ID', 'x')
#('ID', '=')
#('INT', 10)
#('ID', ';')
#('ID', 'int')
#('ID', 'y')
#('ID', '=')
#('INT', 20)
#('ID', ';')
#('ID', 'int')
#('ID', 'z')
#('ID', '=')
#('ID', 'x')
#('ID', '+')
#('ID', 'y')
#('ID', ';')
#('ID', 'System')
#('ID', '.')
#('ID', 'out')
#('ID', '.')
#('ID', 'println')
#('ID', '(')
#('STRING', '"El resultado es: "')
#('ID', '+')
#('ID', 'z')
#('ID', ')')
#('ID', ';')
#('ID', '}')
#('ID', '}')
#Árbol de análisis sintáctico:
#['declaration', 'declaration', 'declaration', ('binary_operation', '+', ('variable', 'x'), ('variable', 'y'))]
