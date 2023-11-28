import ply.lex as lex

# Lista de tokens
tokens = (
    'ID',
    'INT',
    'FLOAT',
    'STRING',
    'BOOLEAN',
    'SEMICOLON',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'CLASS',
    
)

# Reglas de expresiones regulares para tokens simples
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','

# Regla para identificadores (nombres de variables)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Reglas para números enteros y flotantes
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para cadenas de texto
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Elimina las comillas
    return t

# Palabras clave (tokens reservados)
def t_BOOLEAN(t):
    r'true|false'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)

# Construye el analizador léxico
lexer = lex.lex()



