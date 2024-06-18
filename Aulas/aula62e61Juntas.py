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

print('----------------------------------')

nove_digitos = cpf[:9]
cpf_do_calculo = f'{nove_digitos}{primeiro_digito_do_cpf}{segundo_digito}'
print(cpf_do_calculo)

if cpf == cpf_do_calculo:
    print('CPF é válido')
else:
    print('CPF é inválido')