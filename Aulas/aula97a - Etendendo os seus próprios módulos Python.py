# Etendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não rechonhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

import aula97_m_ # jeito 1
from aula97_m_ import soma, variavel_modulo # jeito 2

print(aula97_m_.variavel_modulo)# jeito 1
print(variavel_modulo)# jeito 2

print(soma(2,5))# jeito 1
print(aula97_m_.soma(2,5))# jeito 2

# não consigo importar coisas fora dessa pasta "Aulas", só o que está dentro do pacote do __main__