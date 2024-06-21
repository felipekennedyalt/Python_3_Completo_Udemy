"""
args - argumentos não nomeados
* - * args (compactamento e desempacotamento)
"""
# Lembre-se de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def args(*args):
    total = 0
    for numero in args:
        total += numero
    return total

args123 = args(1, 2, 3)# resultado é 6
print(args123)

args333 = args(3, 3, 3)# resultado é 9
print(args333)

args777 = args(7, 7, 7)# resultado é 21
print(args777)

argsn = args(70, 71, 72, 75, 77)# resultado é 365
print(argsn)
numeros = 70, 71, 72, 75, 77
numeros2 = 70, 71, 72, 75, 77
print(args(*numeros*3)) # o '*' antes na variável significa desempacotamento. é o que a função 'sum()' faz
print(sum(numeros + numeros2)) #