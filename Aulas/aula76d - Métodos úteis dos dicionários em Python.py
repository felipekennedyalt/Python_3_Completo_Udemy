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
# print(list(pessoa.keys())[0]) # mas podemos converter para lista ou tupla e pegar o valor.

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

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# import copy
# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'c3': [11, 22, 33],
# }
# d2 = d1 # não vai copiar d1 para d2, mas vai fazer d2 apontar para d1
# d3 = d1.copy()# com o método copy(), é feito uma cópia do d1 para o d3, mas isso é uma cópia rasa, ele só vai copiar tudo que é imutável, valores mutáveis não são copiados.
# d3 = copy.copy(d1)# método da biblioteca 'copy', também é uma cópia rasa, 'shallow copy'.
# d4 = copy.deepcopy(d1) # Deep copy, é uma cópia profunda, agora 'd4' é uma cópia total de 'd1'

# d2['c1'] = 1000 #mudando a 'c1' de d2
# print(d1) # d1 vai ser afetado também, pois está apontando pro d1. Isso porque dicionários e listas são valores mutáveis, então temos que ter cuidado ao trabalhar com esses valores
# print(d3) # d3 não copiou a lista, meramente aponta para o mesmo local da lista na memória.
# d1['c3'][0] = 1000 #mudando o valor da lista
# print(d3) # como d3 é uma cópia rasa, sua lista é a mesma da 'd1'.
# #caso eu queira uma copia total, vou ter que importar a biblioteca copy do python e fazer uma deep copy
# print(d4)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pessoa = {
    'nome': 'Felipe', 
    'sobrenome': 'Kennedy',# se criar chaves iguais no dicionário, o que será usado, será o último
    'sobrenome': 'Kennedy2',# se criar chaves iguais no dicionário, o que será usado, será o último
    'sobrenome': 'Kennedy3',# se criar chaves iguais no dicionário, o que será usado, será o último. no casso esse aqui será exibido. e no len(), vai contar somente como 1 chave.
}

# print(pessoa.get('nome')) # se não tiver essa chave ele retorna None
# print(pessoa.get('nome', 'Não existe')) # caso não exista, posso passar um valor padrão pra ele retornar, mas geralmente usaremos o None mesmo.

# pop1 = pessoa.pop('nome')
# print(pessoa)

# ultima_chave = pessoa.popitem() # deleta a última chave.
# print(pessoa)

pessoa.update({# atualiza chaves existentes e cria novas chaves, a nova chave fica em baixo das existentes.(não sei se isso importa)
    'nome': 'novo valor',
    'idade' : '28' ,
    'sobrenome': 'kennedy',
})
pessoa.update(nome='outra forma',idade=29, sobrenome='até mais fácil' )

tupla = ('nome', 'também posso fazer update com tuplas'), ('sobrenome', 'não esqueça de deixar uma virgula sobrando'), # também posso fazer update com tuplas, mas não esqueça de deixar uma virgula sobrando
pessoa.update(tupla)

lista = [['nome', 'também posso fazer update com listas'], ['sobrenome', 'não pode ter uma virgula sobrando, se não vai dar erro']] # também posso fazer update com listas, mas não pode ter uma virgula sobrando, se não vai dar erro
pessoa.update(lista)
pessoa.clear() # apaga tudo
print(pessoa)

 