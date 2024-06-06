"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra você vai conferir se a letra digitada stá na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

# palavra_secreta_1 = 'pão'
# palavra_secreta_2 = 'molho'
# palavra_secreta_3 = 'corda'
# palavra_secreta_4 = 'luva'
# palavra_secreta_5 = 'casa'
# palavra_secreta_6 = 'arroz'
# palavra_secreta = "0"
# escolha_da_palavra = input("Digite um número de 1 a 6, e a palavra secreta será escolhida: ")

# if escolha_da_palavra.isdigit():
#     int(escolha_da_palavra)
#     if escolha_da_palavra is not None and escolha_da_palavra <= 1:
#         if escolha_da_palavra == '1':
#             palavra_secreta = palavra_secreta_1
#         elif escolha_da_palavra == '2':
#             palavra_secreta = palavra_secreta_2
#         elif escolha_da_palavra == '3':
#             palavra_secreta = palavra_secreta_3
#         elif escolha_da_palavra == '4':
#             palavra_secreta = palavra_secreta_4
#         elif escolha_da_palavra == '5':
#             palavra_secreta = palavra_secreta_5
#         elif escolha_da_palavra == '6':
#             palavra_secreta = palavra_secreta_6
#         else:
#             print("houve um erro, tente novamente.")
#     else:
#         print('ERRO!')
# else:
#     print('ERRO!')

# contador_de_tentativas = 0
# while True:
#     letra_do_usuário = input("Digite uma letra: ")
#     if letra_do_usuário in palavra_secreta:
#         print(f'parabens, a letra {letra_do_usuário}, está na palavra secreta, ela apareceu {palavra_secreta.count(letra_do_usuário)} vezes na palavra secreta.')
#         break
#     else:
#         contador_de_tentativas += 1
#         print(f'Que pena, a letra {letra_do_usuário}, não está na palavra secreta')
#         continue
# if contador_de_tentativas != 0 :
#     print(f'você tentou {contador_de_tentativas} vezes até acertar.')

#-------------------------------------------------------------------------------------------------- 
# Correção

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True: #esse while ta causando algum problema con as configs do python
    
    letra_digitada = input('Digite uma letra: ')
    
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print(f'Palavra formada: {palavra_formada}')
            
    if palavra_formada == palavra_secreta:
        
        print('Você ganhou! Parabens!!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Você teve {tentativas} tentativas.')
        letras_acertadas = ''
        tentativas = 0
        