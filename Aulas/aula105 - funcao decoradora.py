# Decoradires com parâmetros
def fabrica_de_decoradores(a, b, c):
    def fabrica_de_funcoes(func): #As decoradoras também podem receber parâmetros, 
        #e também podem ser chamadas de funções de ordem superior, intermas, e nester functions que significa anihadas.
        print('Decoradora 1: Antes da função ser criada.')
        def aninhada(*args, **kwargs):
            print('Aninhada')
            res = func(*args, **kwargs)
            return res #sempre lembrar de retornar o resultado da função original e caso eu mude o que vai retornar, eu mudo aqui.
        return aninhada
    return fabrica_de_funcoes #Aqui eu retorno a função que cria a decoradora. Assim eu tenho acesso a 3 escopos;

# def fabrica_de_decoradores(a, b, c):
#     return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3) #Aqui eu passo os parâmetros para a função que cria a decoradora.
def soma(x, y):
    return x + y

#multiplica = fabrica_de_funcoes(lambda x, y: x * y) # antes de deixar a fabrica de decoradores comm a fabrica de funções.
multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
print(multiplica(10, 5))