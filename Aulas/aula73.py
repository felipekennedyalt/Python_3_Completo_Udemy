"""
Higher Order Functions
Funções de primeira classe
"""
# Nessa aula o professor explicou que posso passar uma função como argumento, e também posso retornar uma função
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'bom dia', 'felipe')
print(v)
