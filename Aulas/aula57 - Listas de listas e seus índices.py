"""
Listas de listas e seus índices
"""
salas = [
    # 0          1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine'], # 1
    # 0         1        2 
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)] # 2
]
print(salas[0][1]) # o primeiro [] é a lista e o segundo [] é o indice dessa lista
print(salas[2][3][3]) # aqui ele pegou o valor dentro da tupla que eu escolhi no terceriro []

for sala in salas:
    print(f'a sala é {sala}')
    for aluno in sala:
        print(aluno)