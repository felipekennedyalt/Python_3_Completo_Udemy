# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista1 = [1, 2, 45, 34, 65, 3, 444, 23,45, ]

# lista1.sort()
# lista1.sort(reverse=True)
# # sorted(lista) tem também essa função, mas ela cria uma copia rasa da lista.
# print(lista1)

# def ordena(item):
    
#     return item['nome']

# def ordena_sobrenome(item):
    
#     return item['sobrenome']

# lista.sort(key=ordena)
# # print(lista)# Python não manja ordenar dicionários
# for item in lista:
#     print(item)
# print()
# lista.sort(key=ordena_sobrenome)    
# for item in lista:
#     print(item)
# print()
#função lambda
lista.sort(key=lambda item: item['nome'])  # O 'lambda' fica no lugar do def, não tem nome e não tem os parêntesis do argumento '()'. não precisa de return. essa função está mexendo na minha lista diretamente e colocando ela em ordem


l1 = sorted(lista, key=lambda item: item['sobrenome'])
l2 = sorted(lista, key=lambda item: item['nome'])
print()

def exibir(lista):
    for item in lista:
        print(item)
    print()
        
exibir(lista)

exibir(l1)

exibir(l2)