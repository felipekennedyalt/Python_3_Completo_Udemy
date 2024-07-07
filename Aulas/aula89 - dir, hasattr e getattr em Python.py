# dir, hasattr e getattr em Python
import pprint

def p(valor):
    pprint.pprint(valor)

metodo = 'upper'
stringuinho = 'Felipe'
p(stringuinho)

#se eu quiser checar se o meu objeto tem um atributo nele
# if hasattr(stringuinho, 'upper'):
if hasattr(stringuinho, metodo):
    p('existe o método upper() aqui')
    # p(stringuinho.upper())
    # p(stringuinho.metodo()) # já que não consigo fazer isso, devo usar o getattr
    # p(getattr(stringuinho, metodo))# vai afirmar que metodo é um metodo da string usando () posso acionar esse metodo
    p(getattr(stringuinho, metodo)())
else:
    p('Não existe o método.')
    