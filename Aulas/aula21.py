# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras (True)
# se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São consideradas falsy (que você ja viu) os valores:  0, 0.0, ''(string vazia) False
# Também existe o tipo None que é usado para representar em não valor

# or - Uma das condições precisa ser verdadeira (True)
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# Também existe o tipo None que é usado para representar em não valor

# entrada = input('[E]ntrar [S]sair: ')
# senha_digitada = input("Senha: ")

# senha_permitida = '123'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Acesso permitido')
# else:
#     print('Acesso negado')
    
print(True and False and True)
print(True and 0 and True)