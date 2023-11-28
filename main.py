from AnalizadorLéxico import lexer
from AnalizadorSintáctico import parser

# Lee el código Java desde un archivo
with open("java_code.java", "r") as file:
    java_code = file.read()

# Realiza el análisis léxico
lexer.input(java_code)

# Imprime los tokens encontrados
print("Tokens encontrados:")
for tok in lexer:
    print(tok)

# Realiza el análisis sintáctico
result = parser.parse(java_code)
print("\nÁrbol de análisis sintáctico:")
print(result)

