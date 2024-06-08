"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar, e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
lista_do_usuário = []

while True:
    selecao_do_usuario = input("Selecione uma opção: \n[i] inserir [a] apagar [l] listar: ")
    
    if selecao_do_usuario == 'i':
        adicionar_na_lista = input("Digite o que quer adicionar: ")
        lista_do_usuário.append(adicionar_na_lista)
        for numeracao, valor in enumerate(lista_do_usuário):
            print(numeracao, valor)
        
    if selecao_do_usuario == 'a':
        indice_a_apagar = input('Digite o indice que quer apagar: ')
        if indice_a_apagar.isdigit() and int(indice_a_apagar) <= len(lista_do_usuário):
            print(f'Você apagou o valor {lista_do_usuário.pop()}')
            print('Sua lista agora é: ')
            for numeracao, valor in enumerate(lista_do_usuário):
                print(numeracao, valor)
        else:
            print("Digite um índice válido.")
    
    if selecao_do_usuario == 'l' and len(lista_do_usuário) > 0:
        print('Sua lista agora é: ')
        for numeracao, valor in enumerate(lista_do_usuário):
                print(numeracao, valor)
    else:
        print('Não há nada na lista.')
    
#perfeito ##