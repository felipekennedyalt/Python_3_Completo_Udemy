
# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

# print(platform)
# exit()


"------------------------------------------------------------------------------------------------------------"

#import sys # importa todo o modulo sys
#from sys import exit, platform # se quiser importar variáveis específicas, mas assim a variável fica sem proteção e se eu criar uma variável com o mesmo nome a do "sys" vai ser sobrecrita
# import sys as sis # também da pra colocar um apelido no módulo, mas não é recomendado.
from sys import exit as ex, platform as pt # posso colocar apelidos nas variáveis e classes também
# from sys import * # essa é uma má prática, pois importei tudo mas ficou tudo sem a proteção do "sys"

# exemplo do sys
# sys.exit()#vai sair do programa, mesmo se eu tiver um código abaixo ele não será executado pois eu saí do programa.
# quando importar o módulo inteiro sempre terei que usar o seu NameSpace chamando "sys", isso é bom porque eu poderia ter uma variável com o mesmo nome de uma variável do "sys"
# print(sys.platform) # mostra a plataforma que estou usando, no meu caso diz "win32"
# importando somente as variáveis que eu quero, consigo usar sem chamar o "sys" 
#exit() #assim
#print(platform) ou assim