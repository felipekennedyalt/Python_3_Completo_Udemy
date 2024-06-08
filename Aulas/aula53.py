"""
enumerate - enumrera iteráveis (Índices), o que a gente fez na aula50.py
"""

lista = ['Felipe', 'Kennedy', 'Alencar', 'Mesquita']
lista.append('João')

#lista_enumerada = enumerate(lista) # então o certo é não colocar na variável e sim fazer o enumerate diretamente, assim ele não esgota mais



print(enumerate(lista))
print(next(enumerate(lista)))


for item in enumerate(lista):   
    print(item)
    print('------------')
    
for item in enumerate(lista):
    print(item)
print('o que tem na lista enumerada', enumerate(lista)) #não tem nada pois ja foi consumida pelo for, e pelo print(next(lista_enumerada))

print('-------------------------------------------')

lista_enumerada = list(enumerate(lista))
lista_enumerada = list(enumerate(lista, start=20)) # o enumerate numera cada item da lista, então da pra mudar a numeração dos indices, mas não o indice
#exemplo 
# print(lista_enumerada[0]) # vai dar (20, 'Felipe)
#print(lista_enumerada[20]) # vai dar um erro pos não há indice 20

# o enumerate precisa criar uma lista ou tupla com o indice e o valor, ele cria uma tupla, pois é mais eficiente e coloca os valores nessa tupla. exmplo: (0, 'Felipe)
print(lista_enumerada)

print('-------------------------------------------')

for item in enumerate(lista):
    numeracao, nome = item #desempacotamento
    print(numeracao, nome)
print('-------------------------------------------')

for numeracao, nome in enumerate(lista): # desempacotamento, os criadores do python querem facilitar as coisas.
    print(numeracao, nome)