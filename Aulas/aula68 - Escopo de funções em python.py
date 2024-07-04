"""
Escopo de funções em python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""
x = 1 # 'x' do módulo

def escopo():# o que eu defino dentro da função não pode ser alterada fora da função
    global x # ao dizer que 'x' é global ela permito essa função alterar o valor de 'x', mas somente nessa função, a outra_funcao() ainda está no seu proprio escopo e não consegue alterar o 'x' do módulo
    x = 10 # como o escopo da função é como seu próprio mundo fechado, esse 'x', é diferente do 'x = 1' no inicio do código, caso seja executada a função ela vai dar prioridade ao que está em seu escopo. Se eu colocal o 'x' como global na outra_funcao(), ela também vai conseguir mudar o valor de 'x' do módulo.
    def outra_funcao():
        x = 11
        y = 2 # a funcao escopo não consegue acessar o 'y' pois ela está no escopo a outra_funcao()
        print(x,y)
    outra_funcao() # como eu estou chamando essa outra função aqui, ao acionar a função 'escopo()', essa outra_funcao() também será acionada
    print(x)
    
# def escopo():
#     x = 1
#     print(x)   
#print(x) # vai dar erro pois ta fora da função, enquanto o 'x' ta la dentro

print(x)# vai pegar só o primeiro 'x' 
escopo()# vai pegar só o 'x' no escopo da função
print(x)# vai pegar só o primeiro 'x' 
