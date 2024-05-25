'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Felipe'
preco = 1000.95897643
variavel = 'Felipe, o preço total foi R$1000.95'# assim que vai ficar no final
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x' % (1500, 1500))
print('O hexadecimal de %d é %04x' % (15, 15))