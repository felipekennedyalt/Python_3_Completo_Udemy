# Métodos úteis dos dicionários em Python
# len() - quantas chaves
# keys() - Retorna um iterável com as chaves do dicionário
# values() - Iterável com os valores
# items() - Iterável com os pares chave-valor
# setdefault() - Retorna o valor de uma chave, se não existir, cria uma chave com o valor especificado
# copy() - retorna uma cópia rasa (shallow copy)
# get() - Retorna o valor de uma chave, se não existir, retorna um valor padrão 'None'
# pop() - apaga um item com a chave especificada
# popitem() - apaga o último item adicionado
# update() - Atualiza o dicionário com outro dicionário
# clear() - apaga todos os itens do dicionário
# em python tudo é um objeto, dicionário não deixa de ser um objeto, objetos têm métodos, métodos geralmente estão dento de objetos

pessoa = {
    'nome': 'Felipe', 
    'sobrenome': 'Kennedy',# se criar chaves iguais no dicionário, o que será usado, será o último
    'sobrenome': 'Kennedy2',# se criar chaves iguais no dicionário, o que será usado, será o último
    'sobrenome': 'Kennedy3',# se criar chaves iguais no dicionário, o que será usado, será o último. no casso esse aqui será exibido. e no len(), vai contar somente como 1 chave.
}

# print(pessoa.__len__())# da pra saber quantas chaves tem no dicionário usando o dunder len, que é os duas underlines no inicio e no fim do método '__len__'
# print(len(pessoa))
# print(pessoa['sobrenome'])

# print(pessoa.keys()) # mostra as chaves que eu tenho. se usar o for, ele já pega as chaves 
# # for chave in pessoa.keys(): # se usar o for, ele já pega as chaves
# #     print(chave)   
# #print(pessoa.keys()[0]) # Não funciona pois keys() não é uma lista ou tupla.
#print(list(pessoa.keys())[0]) # mas podemos converter para lista ou tupla e pegar o valor.

# print(pessoa.values())# O keys() mostrava as chaves, esse aqui mostra os valores. oque posso fazer com o keys() também posso fazer com values()
# for valores in pessoa.values():
#     print(valores)

# print(pessoa.items()) # vem as chaves e os valores, também da pra converter em lista ou tupla e usar o for.
# for itens in pessoa.items():
#     print(itens)
# for chave, valor in pessoa.items():
#     print(chave, valor)

# pessoa.setdefault('idade', None) # coloca um valor padrão declarado caso a chave não exista.
# print(pessoa['idade'])

# print(pessoa)

# print(pessoa)
# print(pessoa)
# print(pessoa)