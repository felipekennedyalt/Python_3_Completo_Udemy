"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'a'
# v3 = 'b'
# print(id(v1))
# print(id(v2))
# print(id(v3))

# condcao = False

#if condicao:
#    print('faça algo')
# else:
#    print('não faça nada')


condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça Algo')
else:
    print('Não faça nada')
    
print(passou_no_if, passou_no_if is None) # 'is' é semelhante a '==', mas com none geramente se usa o 'is'
print(passou_no_if, passou_no_if is not None) # 'is' é semelhante a '==', mas com none geramente se usa o 'is'

if passou_no_if is None:
    print('Não passou no if')
if passou_no_if is not None:
    print('Passou no if')
    
    