# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from dados import produtos
from copy import deepcopy

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} # "{**p}" gera um dicionário e expande os produtos
     for p in deepcopy(produtos) # a deep copy aqui não seria necessária, pois não daria pra mudar a lista original com esse código, mas dependendo de como você fizer, da
    
                  ]

produtos_ordenados_por_nome = sorted(
    deepcopy(produtos), # a deep copy aqui não seria necessária, pois não daria pra mudar a lista original com esse código, mas dependendo de como você fizer, da
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenados_por_preco = sorted(
    deepcopy(produtos), # a deep copy aqui não seria necessária, pois não daria pra mudar a lista original com esse código, mas dependendo de como você fizer, da
    key = lambda p: p['preco']
)

print(produtos, sep='\n')
print()
print(novos_produtos, sep='\n')
print()
print(produtos_ordenados_por_nome, sep='\n')
print()
print(produtos_ordenados_por_preco, sep='\n')

