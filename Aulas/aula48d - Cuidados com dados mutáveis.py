"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Felipe' #isso vai ser coletado pelo garbage colector do python pois não vai mais ser utilizado. mas eu dei esse valor pra outra variavel então ainda vai ficar por aqui
# #nome[1] = 'D' # vai gerar erro pois string é imutável ---- TypeError: 'str' object does not support item assignment
# outra_variavel = nome
# nome = 'Kennedy'
# print(nome, outra_variavel)


lista_a = ['Felipe', "Kennedy"]
lista_b = lista_a # aqui lista_b não recebe o valor de lista_a, ele simplesmente aponta para o mesmo local de memória. Então se mudar o lista_a vai mudar na b também.
lista_b = lista_a.copy() # agora que eu copiei a lista a isso não acontece mais. agora são duas listas separadas
lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)