"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('felipe')# .__iter__() entrega o objeto interado, que não é a minha string
#for letra in texto
texto = 'felipe'# Iterável
iterador = iter(texto) # Iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break isso que o for faz em baixo dos panos. pega o iterador mostra no print e quando chega ao final do texto e não tem mais o que mostrar ele cai no break para não dar o erro de StopIteration.

for letra in texto:
    print(letra)# isso que está sendo feito nesse while

# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))
# # print(texto.__next__())
# # print(texto.__next__())
# # print(texto.__next__()) # __ (dois underlines é chamado de dunder)
# # print(texto.__next__()) #como acabou os valores, quando chamar o next de novo vai dar um erro
