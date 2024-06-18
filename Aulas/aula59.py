# Desempactoramento em chamadas 
# de métodos e funções 

string = 'ABCD'
lista = [ 'Maria', 'Helena', 1, 2, 3, 4,  'Eduarda']
tupla = 'python', 'é', 'legal'
salas = [
    # 0          1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine'], # 1
    # 0         1        2 
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)] # 2
]

# p, b, *_, u = lista
# print(p,u, _)

# for nome in lista:
#     print(nome, end=' ')
# print(' ')
# print(*lista)# isso aqui faz amesma coisa do for no desempacotamento da lista
# print(*string)
# print(*tupla)

print(*salas, sep='\n')