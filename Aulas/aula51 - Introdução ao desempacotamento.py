"""
Introdução ao desempacotamento
"""

# nomes = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita']
# nome1, nome2, nome3, nome4 = nomes

nome1, nome2, nome3, nome4 = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita'] # precisamos do mesmo numero de valores, e o mesmo numeros de variáveis pra usar isso, senão vai causar um erro

nome_primeiro, *resto = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita'] # caso eu queira uma variável e deixar o resto numa lista
nome_primeiro, *_ = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita'] # Essa underline(_) serve para dizer que é uma variável que eu não vou usar. essa é uma convenção dos devs de python
#ela ainda funciona, só significa que eu não vou usar

_, nome_segundo, *_ = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita'] # pra escolher um valor sem ser o primeiro
_, nome_segundo, _, _, *_ = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita'] # mesmo não tendo mais valores, a variável *_ continua funcionando, ela só vai receber uma lista vazia.


print(nome_primeiro)
print(nome_segundo)
print(resto)
