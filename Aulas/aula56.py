"""
split e jois com list e str
split - divide uma string
join - une uma string
"""

frase = '     Olha    só que,    coisa    interessante    '
lista_frases_crua = frase.split()

# lista_de_palavras = frase.split() # separa cada palavra em uma lista, separa a partir do espaço
# lista_de_palavras2 = frase.split(',') # coloquei pra quebrar na ',' e não no espaço
# lista_de_palavras3 = frase.split('a') # coloquei pra quebrar no 'a' e não no espaço e o a fica cortado
# print(lista_de_palavras)
# print(lista_de_palavras2)
# print(lista_de_palavras3)

lista_frase = []
# for i, frase in enumerate(lista_de_palavras):
#     #print(f'Frase {i+1}: {frase}')
#    # print(lista_de_palavras[i].strip()) # strip() tira os espaços sobrando no começo e no fim. e tem o lstrip() e o rstrip(), que cortam os espaços na esquerda e direita respectivamente
#     lista_de_palavras[i] = lista_de_palavras[i].strip()
#     print(lista_de_palavras[i])

for i, frase in enumerate(lista_frases_crua):
    lista_frase.append(lista_frases_crua[i].strip()) # ta separando nos espaços por causa do split
print(lista_frases_crua)
print(lista_frase)

frases_unidas = '^^^^^^'.join(lista_frase)
print(f'frases unidas: {frases_unidas}')