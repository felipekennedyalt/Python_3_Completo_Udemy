"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""
# não sabia exatamento como ele queira fazer então vi pelo dele. dava pra fazer de várias formas, com o if por exemplo. o professor fez criando uma função que cria funções

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
