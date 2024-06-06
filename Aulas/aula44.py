"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(10)
# numeros = range(5, 10)
# numeros = range(5, 10, 2)# inicia em 5 vai até 10 no caso para no 9, e pula de 2 em 2
# numeros = range(10, 0, -1)# indo ao contrário
# numeros = range(0, 100, 8)#multiplos de 8 de 0 a 100


for numero in numeros:
    print(numero)