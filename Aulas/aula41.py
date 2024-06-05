""" while / else"""

string = 'Valor qualquer'

i= 0

while i < len(string):
    letra = string[i]
    
    print(letra)
    i += 1
    #break ----- se tiver um break no meio o resto do código não vai ser executado.
    # if letra == ' ':        #com esse código eu poderia colocar no else "não encontrei espaço na string"
    #     break
else:
    print("O else foi executado.")
print('Fora do while.')