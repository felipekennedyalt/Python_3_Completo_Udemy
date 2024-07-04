# isinstance - para saber se o objeto é de determinado tipo
listinha = ['a', 1 , 1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Felipe'},]

for item in listinha:
    if isinstance(item, set):
        print('set = ')
        item.add(5)
        print(item, isinstance(item, set))
        
    elif isinstance(item, str):
        print('str = ')
        print(item.upper(), isinstance(item, str))# como str é imutável não deixei o A maiúsculo na lista e sim no print, pra deixar na lista ia precisar pegar o indice e mudar ele dentro da lista
        
    elif isinstance(item, (int, float)):
        print('num = ')
        print(item, item * 2)
    
    else:
        print('Outro:', item, type(item))