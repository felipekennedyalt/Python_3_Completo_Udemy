"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

def multiplicacao_de_args(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def impar_par(*args):
    for numero in args:
        if numero % 2 == 0:
          resultado =  f'O número {numero} é par'
        else:
          resultado = f'O número {numero} é ímpar'
        return resultado

valor_da_multilpicacao = multiplicacao_de_args(1, 3, 3, 3, 3, 9)
print(f'O valor da multiplicação é {valor_da_multilpicacao}')

impar_ou_par = impar_par(valor_da_multilpicacao)
print(f'{valor_da_multilpicacao} | {impar_ou_par}')