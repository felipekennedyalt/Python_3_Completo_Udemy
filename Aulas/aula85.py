lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))# quero colocar dois valores por indice na lista, por isso adiciono uma tupla com ()
lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
    
]
lista = [
    [(x, y) for y in range(3)]# pra cada x ta fazendo uma nova lista
    #[letra for letra in 'Luz']# pra cada x ta fazendo uma nova lista
    for x in range(3)
    for y in range(3)
    
]
print(lista)