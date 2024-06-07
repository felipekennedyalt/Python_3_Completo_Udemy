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
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Felipe')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear() #apagatudo e limpa a lista
lista.insert(0, 5) # primeiro argumento é o indice que eu escolhi pra dar o insert, e o segundo argumento é o valor.
lista.insert(0, 'Felipe Kennedy') # primeiro argumento é o indice que eu escolhi pra dar o insert, e o segundo argumento é o valor.

# print(lista[10]) #IndexError: list index out of range ------- quer dizer quenão tem esse indice na lista
lista.insert(50000, 555) # caso a lista não tenha o indice especificado, não gera erro, só faz o valor ir pro final da lista.

print(lista, nome)