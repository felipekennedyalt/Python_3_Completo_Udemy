"""
Calculo do segundo dígito do CPF
CPF : 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
mais o PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.: 746.824.890.70 (7468248907)
     11 10 9  8  7  6  5  4  3  2
     7  4  6  8  2  4  8  9  0  7  <--- PRIMEIRO DÍGITO
     77 40 54 64 14 24 40 36 0  14

Somar todos os resultados:
77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anteior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
O segundo dígito do CPF é 0
"""

cpf = '74682489070'
intera = 0
regressiva_2 = 11
soma_dos_9 = 0
while intera <= 9:
    multiplicacao_dos_9 = int(cpf[intera]) * (regressiva_2 - intera)
    intera += 1
    print(multiplicacao_dos_9, end=' ')
    soma_dos_9 +=  multiplicacao_dos_9
print()
print(f'A multiplicando cada um dos valores por uma contagem regressiva começando de 11 e sua soma é igual a = {soma_dos_9}')

multiplica_por_10_2 = soma_dos_9 * 10
resto_2 = multiplica_por_10_2 % 11
if resto_2 > 9:
    segundo_digito = 0
    print(f'O segundo dígito do CPF é 0')
else:
    segundo_digito = resto_2
print(f'O segundo dígito é = {segundo_digito}')