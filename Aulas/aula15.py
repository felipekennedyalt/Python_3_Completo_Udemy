# nome = input('Qual o seu nome? ')
# print(f'Olá {nome}! Seja bem-vindo(a) ao curso de Python!')

# numero_1 = int(input('Digite um numero: ')) # não pode fazer isso pois se o usuario digitar uma str ao invez de um int vai gerar erro, temos que fazer uma checagem que vamos aprender depois
numero_1 = input('Digite um numero: ')
numero_2 = input('Digite um outro numero: ')

# isso ainda vai quebrar caso o usuario digite algo que ão deve, mas pelo menos poderemos checar o que ele digitou. 
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos numeros é {int_numero_1 + int_numero_2}')
