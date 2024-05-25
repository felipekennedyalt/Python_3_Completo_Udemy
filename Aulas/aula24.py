# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# F e l i p e 
# -6-5-4-3-2-1

# nome = 'Felipe'
# print(nome[0])
# print(nome[-5])
# print('e' in nome)
# print('z' in nome)
# print('pl' in nome)
# print('Fe' in nome)
# print('fe' in nome)
# print('fe' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está no nome {nome}')
else:
    print(f'{encontrar} não está no nome {nome}')