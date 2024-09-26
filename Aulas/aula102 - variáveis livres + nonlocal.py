# variáveis livres + nonlocal
#globals() # mostra as variáveis globais
import pprint

def p(valor):
    pprint.pprint(valor) # def pra fazer o pprint funcionar só com o 'p'
# def fora(x):
#     a = x # essa é a variável livre
    
#     def dentro():
#         #print(locals()) # locals() vai me mostrar quais variáveis são locais da função dentro()
#         #print(dentro.__code__.co_freevars) # vai me mostrar quais variáveis são livres
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(120)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial
    
    #def interna(valor_a_concatenar):
    def interna(valor_a_concatenar = ''):# na variável "final", se eu não passar nenhum parâmetro vai dar erro, "valor_a_concatenar = ''" assim não da
        nonlocal valor_final # 2º agora não vai mais gerar erro, pois a variável não é mais local, do mesmo jeito que da pra tornar a variável global usando o "global valor_final"
        valor_final += valor_a_concatenar # 1º vai gerar um erro, pos posso ler a variável "valor_final" mas não posso muda-la, pois ela não é desse escopo
        return valor_final # valor_final é uma variável livre pois não está definada dentro do escopo da interna
    return interna

c = concatenar('a')

p(c('b'))
print(c('c'))
p(c("d"))
final = c()
p(final)

# basicamente a aula foi pra ensinar como usar variáveis não locais