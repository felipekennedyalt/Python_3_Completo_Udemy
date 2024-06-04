"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = 0

while contador <= 20:
    
    contador += 1
    
    if contador == 13:
        print('não vou mostrar o 13')
        continue
    
    
    if contador == 11:
        print('não vou mostrar o 11')
        continue
    
    
    if contador == 12:
        print('não vou mostrar o 12')
        continue
    
    if contador >= 5 and contador <= 10:
        print(f'não vou mostrar o {contador}')
        continue
    
    print(contador)
    if contador == 14:
        break
    
print("Acabou")