"""
Closure e funções que retornam outras funções
"""

#def criar_saudacao(saudacao, nome):
def criar_saudacao(saudacao):
    #def saudar():
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

criar_bom_dia = criar_saudacao('Bom dia')
#s1 = criar_saudacao('Bom dia', 'Felipe')

#s2 = criar_saudacao('Boa noite', 'Felipe')
Criar_boa_noite = criar_saudacao('Boa noite')

#print(s1())
print(criar_bom_dia('Felipe'))
print(Criar_boa_noite('Felipe'))
#print(s2())

for nome in ['maria', 'bonfim', 'alex']:
    print(criar_bom_dia(nome))
    print(Criar_boa_noite(nome))
#usamos uma função pra criar mais funções