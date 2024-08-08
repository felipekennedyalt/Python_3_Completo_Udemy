# Try, except, else e finally

# try tenta executar um código. try não consegue viver sozinho então precisa de um desses (except, else e finally)(try e else sozinhos não funciona)
a = 18
b = 0
#c= a/b # se o usuário colocar uma divisão com 0 como está aqui isso vai dar um erro e crashar o código.  
# try:
#     print("linha 1")
#     c= a / b
#     print("linha 2")
# except ZeroDivisionError:# aqui se der um erro causado por divisão por zero, aí vai exibir o print.
#     print("dividiu por 0") # assim não é bom pos precisa informar qual o erro que essa except está tratando, e podem ser vários.
# except NameError:# aqui se der um erro causado por causa do nome, aí vai exibir o print.
#     print("Nome não está definido")
# except (NameError, ZeroDivisionError):# se tiver 2 erros conhecidos posso fazer assim com uma tupla
#     print("Nome não está definido")
# print("continuar")
# exeções são classes que representa merros.
# a maior classe de xeção é a "Exception", qualquer erro que acontecer vai cair no "Exception"
try:
    18 / 0
except Exception:
    print("Erro desconhecido")