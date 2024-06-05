""" Calculador com while """

num_1 = input("Digite o número 1: ")
num_2 = input("Digite o número 2: ")
operador = input("Digite o operador (+ - / *): ")
pode_no_operador = "(+-/*)"

while num_1.isdigit() and num_2.isdigit() and operador is not None:
    num_1_float = float(num_1)
    num_2_float = float(num_2)
    calculo = 0
    
    if operador == '+' :
                calculo = num_1_float + num_2_float
                print(f'Seu calculo é {calculo}')
    elif operador == '-' :
                calculo = num_1_float - num_2_float
                print(f'Seu calculo é {calculo}')
    elif operador == '*' :
                calculo = num_1_float * num_2_float
                print(f'Seu calculo é {calculo}')
    elif operador == '/' :
                calculo = num_1_float / num_2_float
                print(f'Seu calculo é {calculo}')
    else:
                print('Operador inválido')
            
        
    break
if num_1.isdigit() == False or num_2.isdigit() == False:
    print("Digite números válidos.")   
    
if operador not in  pode_no_operador:
    print("digite um operador válido.") 
