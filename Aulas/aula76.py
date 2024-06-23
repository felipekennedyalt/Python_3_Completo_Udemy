"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutáveis: list, dict
pessoa = {
    'nome': 'Felipe',
    'sobrenome: 'Kennedy',
    'idade': 28,
    'altura': '1.69',
    'endereços':[
        {'rua': 'Rua 1', 'numero': 123},
        {'rua': 'Rua 2', 'numero': 456},
    ]
    
}
print(pessoa, type(pessoa))
"""
pessoa = {
    'nome': 'Felipe', # dentro do dicionário se usa ':' e não o sinal de igual '=', mas se eu fizer usando a função dict(), então é com '=' ex.: pessoa = dict(nome='felipe', idade=18)
    'sobrenome': 'Kennedy',
    'idade': 28,
    'altura': 1.69,
    'endereços':[
        {'rua': 'Rua 1', 'numero': 123},# aqui tenho uma lista com vários dicionarios dentro registrando o endereço
        {'rua': 'Rua 2', 'numero': 456},
    ]
}
#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave,pessoa[chave])