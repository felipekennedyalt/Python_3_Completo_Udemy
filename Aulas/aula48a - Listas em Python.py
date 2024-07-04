"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, Create, Read, Update, Delete
                                                        criar,  ler,  alterar, apagar = lista[i] (CRUD)
"""

lista = [10 , 20 , 30, 40]

# lista[2] = 300

# del(lista[2]) #  o python pode ficar lento ao rearranjar a lista por deletar um valor e ter que rearranjar os posteriores na lista. Exemplo: tem uma lista de 100000 valores e deleto o 2º, vai ter que fazer os outros que vêm depois todos mudarem de indice para acomodar a mudança
# #é mais interessante trabalhar com o final da lista pra evitar esse tipo de coisa.

# print(lista)
# print(lista[2])

lista.append(50) # append adiciona um valor no final da lista, pode ser executado quantas vezes você quiser e facilita o trabalho do python evitando a situação exemplificada.
lista.pop() #pop remove o ultimo elemento da lista, como no momento o ultimo elemento é o 50, ele será removido
lista.append(60)
lista.append(70)
#ultimo_valor = lista.pop() # o pop() retorna o ultimo valor removido, então da pra vizualizar ou guardar esse elemento em uma variável para fazer algo ocm ele depois.
ultimo_valor = lista.pop(3)  # da pra escolher o indice da lista que eu quero remover.
print(lista, 'Removido', ultimo_valor)