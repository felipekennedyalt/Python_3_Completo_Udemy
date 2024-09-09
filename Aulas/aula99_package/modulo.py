__all__ = [# aqui eu escrevo as variávei que eu quero que apareça ao usar o import com a *
    'variavel',
    'soma_do_modulo'
]

variavel = 'alguma coisa'

def soma_do_modulo(x , y):
    return x + y

nova_variavel = 'não existe' # se eu não descrever essa variável no __all__, ela não aparece no __main__ com o import *