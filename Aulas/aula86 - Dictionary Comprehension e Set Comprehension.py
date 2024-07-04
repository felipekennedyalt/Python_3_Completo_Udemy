# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {# copiando o dicionário 'produto'
    #chave: valor 
    chave: valor # tenho um float em um dos valores, então vou precisar fazer um if pra não dar erro
    if isinstance(valor, (int, float)) else valor.upper() #No Python posso checar se algo é de um determinado valor usando isinstance() # se int ou float vai executar, se não vai passar o valor em maiúsculo
    for chave, valor
    in produto.items()
    if chave == 'categoria' # nesse caso, só vai incluir categoria
}

print(dc)

listinha = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

print(dict(listinha))# já que minha listinha parece um dicionário, com uma chave e um valor posso 'converter'

s1 = {i ** 3 for i in range(10)}

print(s1)