"""
Peça ao usuário para digitar seu nome e idade
se forem digitados:
        Exiba:
            Seu nome é {nome}
            seu nome invertido é {nome invertido}
            se nome contém (ou não) espaços
            Seu nome tem {quantidade de letras} letras
            A primeira letra do seu nome é {letra}
            a última letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome_usuario = input('Digite seu noome: ')
idade_usuario = input('Digite sua idade: ')

len_nome_usuario = len(nome_usuario)
espaco = ' '
if nome_usuario != None and idade_usuario != None: #podia fazer : if nome and idade: porque se não tivesse nada dentro ia dar como False, pelo bool
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    if espaco in nome_usuario:
        print(f'Você tem espaço(s) no seu nome {nome_usuario}')
    else:
        print(f'Você não tem espaço(s) no seu nome {nome_usuario}')
    print(f'Seu nome tem {len_nome_usuario} letras')
    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A última letra do seu nome é {nome_usuario[len_nome_usuario-1]}')
else:
    print('Desculpe, você deixou campos vazios.')