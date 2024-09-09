# Etendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não rechonhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
import sys
import aula97_m_

print("este módulo se chama ", __name__)
print(*sys.path, sep='\n')

sys.path.append('Users/felipe/Desktop')# se eu quisesse usar um pacote que não está aqui desntro do pacote atual, ('Users/felipe/Desktop') é o caminho do pacote