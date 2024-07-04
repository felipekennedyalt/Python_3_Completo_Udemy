"""
Exercício
Exiba os índices da lista
resultado esperado
0 Felipe
1 Kennedy
2 Alencar
3 Mesquita
"""

lista = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita']
lista.append(' João')
indice_meu = 0
for nome in lista:
    print(f'O índice do nome {nome} é {indice_meu}')
    indice_meu += 1 # assim deu certo, mas ele pensou de outra forma, então vou fazer também

#--------------------------------------------------------------------------------------------
#resolução do professor
indices = range(len(lista))
print(indices)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    