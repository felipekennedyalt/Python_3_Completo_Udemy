# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5) # essa função vai somar com 5 todo numero que você passar
multiplica_por_dez = criar_funcao(multiplica, 10) # essa função vai multiplicar por 10 todo numero que você passar