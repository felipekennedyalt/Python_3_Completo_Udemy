"""
Valores padrão para parâmetros
ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar seu código.
"""
# Definição
def soma(x, y, z=None): # o que vier depois de uma valor padrão também deve receber um valor padrão
    if z is not None:
        print(f'{x=} {y=} {z=}', '|','x + y + z =', x + y + z)
    else:
        print(f'{x=} {y=}', '|', 'x + y =', x + y)

soma(1, 2)
soma(10, 20)
soma(100, 200)
soma(100, 200, 0)
