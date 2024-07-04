# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a,b = b, a# isso aqui é o empacotamento
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa
# print(a, b)

# a, b = pessoa.values()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()# isso
# print(a1, a2, b1, b2)
# for chave, valor in pessoa.items():# é igual a isso
#     print(chave, valor)

dados_pessoa ={
    'idade': 16,
    'altura': 1.6,
}

# para juntar os dicionários, posso criar um terceiro dicionário e extrair os valores (**)
pessoa_completa = {**pessoa, **dados_pessoa, 'chave': 1, 'nome': 'Lurdes'}
# print(pessoa_completa)


# args e kwargs
# args (já vimos)
# Kwargs - Keyword arguments (argumentos nomeados)

def mostrar_agumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
    
# mostrar_agumentos_nomeados(1,2,nome='joana', qlq=123)
mostrar_agumentos_nomeados(**pessoa_completa)