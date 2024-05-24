# if / elif     / else
# se / se não se / se não
entrada = input('Você quer "entrar", ou "sair"? ').lower() # lower() transforma tudo em minusculo

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Entrada inválida.')

print('Fora dos blocos if, ifelse, else. o código tem que estar dentro dos blocos para fazer parte deles.-')
