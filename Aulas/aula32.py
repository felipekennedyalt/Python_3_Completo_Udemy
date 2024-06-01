"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, 
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

num_inteiro_user = input("Digite um número inteiro: ")

if num_inteiro_user.isdigit() and not None:
    num_inteiro_user = int(num_inteiro_user)
    num_inteiro_user_impar_ou_par = num_inteiro_user % 2
    if num_inteiro_user_impar_ou_par == 1:
        print(f"O número {num_inteiro_user} é impar")
    if num_inteiro_user_impar_ou_par == 0:
        print(f'O número {num_inteiro_user} é par')
else:
    print(f" {num_inteiro_user} não é um número inteiro")

# -------------------------------------------------------------------------------------------------------------------
usurario_digita_hora = input("Digite a hora: ")

if usurario_digita_hora.isdigit() and not None:
     usurario_digita_hora_int = int(usurario_digita_hora)
try:
    
    if usurario_digita_hora.isdigit() and not None:
        if usurario_digita_hora_int >= 0 and usurario_digita_hora_int <= 11:
            print("Bom dia")
        elif usurario_digita_hora_int >= 12 and usurario_digita_hora_int <= 17:
            print("Boa tarde")
        elif usurario_digita_hora_int >= 18 and usurario_digita_hora_int <= 23:
            print('Boa noite')
except:
        print("Houve um erro.")
        
# -------------------------------------------------------------------------------------------------------------------

primeiro_nome_user = input("Digite seu primeiro nome: ")
tamanho_nome = len(primeiro_nome_user)

if tamanho_nome >= 1 and tamanho_nome <= 4  and not None:
    print("Seu nome é curto")    
elif tamanho_nome >= 5  and tamanho_nome <=6  and not None:
    print("Seu nome é normal")
elif tamanho_nome >6  and not None:
    print("Seu nome é muito grande")
else:
    print("Houve um erro")