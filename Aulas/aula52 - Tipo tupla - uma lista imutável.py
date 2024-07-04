"""
Tipo tupla - uma lista imutável
"""

nomes = 'Felipe', 'Kennedy', 'Alencar', 'Mesquita' # ao não colocar os colchetes eu crio uma tupla, e a tupla é mais eficiente que a lista. tambem da pra criar a tupla usando () ao invez de [] ou fazendo isso: 
# nomes = tuple(nomes) # converti pra tupla
# nomes = list(nomes) # converti de volta pra lista

#nomes[1] = 'outro' #como a tupla é imutável ela não consegue mudar o valor, assim como o string
_, _, nome, _, *resto = nomes

print(nomes[0])
print(nomes[3])
print(resto)