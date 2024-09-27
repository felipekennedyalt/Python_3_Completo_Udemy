# Exercício - Adiando execução de funções
def soma(x, y): # 'def soma(x, y):' isso é chamado de assinatura da função ou método
    return x + y


def multiplica(x, y):
    return x * y

def divide(x, y):
    return x / y


# def criar_funcao(funcao, *args):
#     def interna(*args):
#         return funcao(*args) # isso é um closure, o soma_com_cinco e o multiplica_por_dez, vão ficar salvos na memória e quando a função terminar vou conseguir acessar ela retornando a def interna
#     return interna
def criar_funcao(funcao, x):# pra ficar mais facil de entender
    def interna(y):
        return funcao(x, y) # isso é um closure, o soma_com_cinco e o multiplica_por_dez, vão ficar salvos na memória e quando a função terminar vou conseguir acessar ela retornando a def interna
    return interna


soma_com_cinco = criar_funcao(soma, 5) # essa função vai somar com 5 todo numero que você passar
multiplica_por_dez = criar_funcao(multiplica, 10) # essa função vai multiplicar por 10 todo numero que você passar
divide_por_dez = criar_funcao(divide, 10) # essa função vai multiplicar por 10 todo numero que você passar

print(soma_com_cinco(10)) # esse número aqui é o 'y'
print(multiplica_por_dez(10)) # esse número aqui é o 'y'
print(divide_por_dez(5)) # esse número aqui é o 'y'
