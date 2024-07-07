# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

import pprint

def p(valor):
    pprint.pprint(valor),
    
# como o return para a função e sai dela, não podemos usar o return para fazer uma função geradora, no seu lugar usaremos o yield

# def generatorzin(n=0):
#     yield 1 # pausar # toda função que tem o yield é uma generator function
#     p('continuando...')
#     yield 2 # pausar
#     p('ainda tem...')
#     yield 3 # pausar
#     return "Acabou" # ainda posso usar o return mas ele funciona de forma diferente agora

    
# gen = generatorzin(n=0)
# # p(next(gen))
# # p(next(gen))
# # p(next(gen))# ao chamar de novo como não vou ter mais valores vai acabar dando 'StopIteration' como coloquei o 'return "Acabou"', vai indicar o valor que eu mandei retornar com o return na mensagem de erro

# # pra fazer dinamicamente
# for n in gen:
#     p(n)
    
# como seria
def generatorzin(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return 'Acabou'
        
gen = generatorzin()# não preciso colocar valor pois já defini valores padrões, mas se quiser posso colocar 'maximum=100000' para sobrepor o valor padrão e fazer o código doar cem mil vezes
for n in gen:
    p(n)