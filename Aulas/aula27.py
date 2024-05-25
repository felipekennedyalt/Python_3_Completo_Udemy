"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'

print(variavel[5])
print(variavel[-4])
print(variavel[4:7])
print(variavel[4:])
print(variavel[0:5])
print(variavel[0:-3])
print(len(variavel[0:-3]))
print(len(variavel))
print(variavel[0:len(variavel):2])#passo, colocando 2 pega um, pula outro e por aí vai
print(variavel[::-2])#passo, colocando 2 pega um, pula outro e por aí vai
print(variavel[-1:-10:-1])#passo, colocando 2 pega um, pula outro e por aí vai