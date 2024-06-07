"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos uteis:
    append - Adiciona um item no final
    insert - Adiciona um iterm no índice escolhido
    pop - Remove do final ou do índoce escolhido
    del - Apaga um índice
    clear - limpa a kista
    extend - estende a lista
    + - cancatena listas
Create, Read, Update, Delete
criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # esse método extendo não retona nada, ele mexeu no próprio lista_a e não retornou valor pra lista_d

print(lista_c)
print(lista_d)
print(lista_a)
lista_a.reverse()
print(lista_a)

