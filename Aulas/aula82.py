# função normal
def executa(funcao, *args):# ta executando as funções, tenho que usar pois de acordo com a pep8 o python me manda criar uma função mesmo
    return funcao(*args)

#daria pra fazer isso, mas é má prática
# funcao = lambda parametro: parametro
# em lambda

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(executa(lambda x, y : x + y,2,3)) # isso
print(executa(soma, 2, 3)) # é igual a isso
soma(2, 3)

duplica = cria_multiplicador(2) # criei uma função que duplica os valores que eu der
print(duplica(20))
#com lambda
duplica_lambda = executa(
    lambda m: lambda n: n * m,
    2 # aqui é pra duplicar, multiplicar por '2'
)
print(duplica_lambda(55))

print(executa(lambda *args: sum(args), 1, 2, 3 ,4))

# lambda é pra algo rápido e fácil, quanto mais legivel e rápido de ler for o seu código melhor.