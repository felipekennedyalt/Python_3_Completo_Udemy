primeiro_valor = input('Digite um valor: ') # lembrando que o input sempre retorna uma string
segundo_valor = input('Digite um outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor=}' 
          f'é maior que o segundo valor {segundo_valor=}'
         )
else:
    print(f'O segundo valor {segundo_valor=}' 
          f'é maior que o primeiro valor {primeiro_valor=}'
         )