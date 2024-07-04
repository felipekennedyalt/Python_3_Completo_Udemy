"""
Cálculo do primeiro dígito do cpf
CPF : 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 746.824.890.70 (746824890)
   10 9  8  7  6  5  4  3  2
   7  4  6  8  2  4  8  9  0
   70 36 48 56 12 20 32 27 0
   
Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 0 =301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anteriror por 11
3010 % 11 = 7
se o resultado anteior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
O primeiro dígito do cpf é 7
"""
primeiro_digito_do_cpf = 0
cpf = '74682489070'
intera = 0
soma_de_todos_da_multiplicacao = 0
while intera <= 8:
    regressivo = 10
    cpf_int = int(cpf[intera])
    multiplicacao = cpf_int * (regressivo - intera)
    intera += 1 
    soma_de_todos_da_multiplicacao += multiplicacao
    print(multiplicacao, end=' ')
print()
print(f'A soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10 é igual a = {soma_de_todos_da_multiplicacao}')

multiplicar_a_soma = soma_de_todos_da_multiplicacao * 10

resto = multiplicar_a_soma % 11
print(f'o resto da divisão da conta anteriror por, Multiplicar o resultado anterior por 10 é igual a = {resto}')
if resto <= 9:
    primeiro_digito_do_cpf = resto
else:
    primeiro_digito_do_cpf = 0
print(f'Assim, o primeiro dígito do cpf é igaul a = {primeiro_digito_do_cpf}')# consegui fazer a atividade