# Pra importar do package é assim
import aula99_package.modulo # jeito 1 # assim é pior
from aula99_package import modulo # jeito 2 # assim é menos pior
from aula99_package.modulo import soma_do_modulo # jeito 3 # assim é melhor
from aula99_package.modulo import * # má pratica

print(aula99_package.modulo.soma_do_modulo( 5 ,7)) # jeito 1 # assim é pior
print(modulo.soma_do_modulo( 5 ,7)) # jeito 2 # assim é menos pior
print(soma_do_modulo( 5 ,7))# jeito 3 # assim é melhor
print(variavel)
# print(nova_variavel)