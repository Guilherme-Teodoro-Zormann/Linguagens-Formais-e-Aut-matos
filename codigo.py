import re

entrada = "3 + 7 - 2 * (4 + 5)"

def reconhecer_tokens(entrada):
    # Expressão regular para separar números, operadores e parênteses
    tokens = re.findall(r'\d+|[+\-*/()]{1}', entrada)
    
    for caractere in tokens:
        if caractere.isdigit():
            print(f"Token: NÚMERO ({caractere})")
        elif caractere in ['+', '-', '*', '/']:
            print(f"Token: OPERADOR ({caractere})")
        elif caractere == '(':
            print(f"Token: PARÊNTESE ABRE ({caractere})")
        elif caractere == ')':
            print(f"Token: PARÊNTESE FECHA ({caractere})")
        else:
            print(f"Token inválido: {caractere}")

# Chama a função com a entrada
reconhecer_tokens(entrada)
