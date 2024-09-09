#esse arquivo é executado assim que o módulo for importado.
print('Você importou o package', __name__)

# engana o python fazendo ele achar qeu tem metodo no package.
def dobra(x):
    return x*2

from .modulo import nova_variavel, variavel, soma_do_modulo
# import * é má pratica mas assim talvez poderia ser usado aqui no init sem muito problema
from aula99_package.modulo import *