"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
# Definição
def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|','x + y + z =', x + y + z)
    
soma(1, 2, 7)
soma(y=1, z=7, x=2)# nomeando as variáveis com os mesmos nomes dos parâmetros ele busca o que você nomeou e não depende mais de ficar em ordem.
soma(1, 2, z=7) # se eu quiser fazer misturando os não nomeados com os nomeado, os que vierem depois do nomeado deverão obrigatoriamente serem nomeado também.