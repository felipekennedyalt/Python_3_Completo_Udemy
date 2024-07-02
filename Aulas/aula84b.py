# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
import pprint

def p(valor):
    pprint.pprint(valor, sort_dicts=False, width=40)
# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [numero for numero in range(10)]
# lista = [
#     numero * 2
#     for numero in range(10)
#          ]
# print(lista)

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preço': 20,},
    {'nome': 'p2', 'preço': 10,},
    {'nome': 'p3', 'preço': 30,},
    
]

# no mapeamento eu pego dados de uma lado, de um iterável, tranformando ou não esses dados, e coloco eles em outra lista com ambas tendo o mesmo tamanho.

novos_produtos = [
    #{'nome': produto['nome'], 'preço': produto['preço']} 
    {**produto, 'preço': produto['preço'] * 1.05} # aumentei o preço em 5%
    if produto['preço'] > 20 else {**produto}
    for produto in produtos#o filtro é depois do for, e não tem else, é so 'if'
    # if produto['preço'] > 10# esse preço não é o novo, ajustado depois do primeiro if, esse preço é o preço original, cuidado
    if produto['preço'] >= 20 and produto['preço'] * 1.05 > 10# pra levar minha condição anterior em conta faço isso:
    ]

# print(*novos_produtos, sep='\n')

p(novos_produtos)

#fazer lista facil com list comprehension
# lista_facil = [n for n in range(10) if n < 6]
# p(lista_facil)

