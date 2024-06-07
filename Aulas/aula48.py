"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +
"""

#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
#lista = list() # da pra fazer lista assim
#lista = str() # do mesmo jeito que da pra fazer string assim
#print(bool(lista)) #falsy se tiver vazia

# indices 0     1           2           3      4
# negat   -5   -4          -3          -2     -1
lista = [123, True, 'Felipe Kennedy', 1.5, ['abc']]
lista[-3] = 'Alencar Mesquita'
print(lista[2], type(lista[2]))
print(lista)
