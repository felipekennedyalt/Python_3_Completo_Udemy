"""
Introdução às funções (def) em Python
Funçõessão trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

def Print():
    print('1')
    
Print()

def imprimir(a, b, c): # esses são os parâmetros, eles ficam aqui
    print(a, b, c)
  
 
imprimir('nome', 'idade', 'pais') # esses são os argumentos, eles que vão para os parâmetros da função
# então ao falar da variavel 'a', me refiro aos parâmetros, ao me referir aos valores, me refiro aos argumentos
imprimir('luiz', 'do', 'som')
imprimir('Felipe', '28', 'Brasil')

def imprimido(nome='Sem nome'):
    print(f'Olá, {nome}!')
imprimido()