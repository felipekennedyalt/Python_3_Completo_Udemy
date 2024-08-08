# Try, except, else e finally

try:
    print("try foi executado")
    18/0
except Exception as e:
    print(e)
else:# se não der erro vai entrar no else, mas se der não vai
    print("não deu erro") 
finally: # finally sempre vai ser executado
    print("finally foi executado")