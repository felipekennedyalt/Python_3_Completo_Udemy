# Exercício - sistema de perguntas e respostas

perguntas = [{
    "Pergunta": "Quanto é 2 + 2?",
    "Opções": ['1', '3', '4', '5'],
    "Resposta": '4',
},
{
"Pergunta": "Quanto é 5 * 5?",
"Opções": ['25', '55', '10', '30'],
"Resposta": '25',
},
{
"Pergunta": "Quanto é 10/2?",
"Opções": ['4', '5', '2', '1'],
"Resposta": '5',
}]

print('Inicio do desafio!')
while True:
    contador = 0
    contagem_de_acertos = 0
    contagem_de_erros = 0
    resposta_certa_pergunta_1 = list(perguntas[0].values())[2]
    print(list(perguntas[0].values())[0])
    for respostas in list(perguntas[0].values())[1]:
        print(f' {contador}) {respostas}')
        contador += 1
    print()

    resposta_do_usuario = input("Responda: ")
    if resposta_do_usuario.isdigit() == True and int(resposta_do_usuario) <= 3:
        resposta_do_usuario = int(resposta_do_usuario)
    else:
        print("Digite um valor válido.")
        break
    print()
    
    if list(perguntas[0].values())[1][resposta_do_usuario] == resposta_certa_pergunta_1:
        print("Você acertou!😄")
        contagem_de_acertos += 1
    else:
        print("Você errou!😓")
        contagem_de_erros += 1
    print()
    #--------------------------------------------------------------------------------------------------------------2
    contador = 0
    resposta_certa_pergunta_2 = list(perguntas[1].values())[2]
    print(list(perguntas[1].values())[0])
    for respostas in list(perguntas[1].values())[1]:
        print(f' {contador}) {respostas}')
        contador += 1
    print()

    resposta_do_usuario_2 = input("Responda: ")
    if resposta_do_usuario_2.isdigit() == True and int(resposta_do_usuario_2) <= 3:
        resposta_do_usuario_2 = int(resposta_do_usuario_2)
    else:
        print("Digite um valor válido.")
        break
    print()
    
    if list(perguntas[1].values())[1][resposta_do_usuario_2] == resposta_certa_pergunta_2:
        print("Você acertou!😄")
        contagem_de_acertos += 1
    else:
        print("Você errou!😓")
        contagem_de_erros += 1
    print()
        #--------------------------------------------------------------------------------------------------------------3
    contador = 0
    resposta_certa_pergunta_3 = list(perguntas[2].values())[2]
    print(list(perguntas[2].values())[0])
    for respostas in list(perguntas[2].values())[1]:
        print(f' {contador}) {respostas}')
        contador += 1
    print()

    resposta_do_usuario_3 = input("Responda: ")
    if resposta_do_usuario_3.isdigit() == True and int(resposta_do_usuario_3) <= 3:
        resposta_do_usuario_3 = int(resposta_do_usuario_3)
    else:
        print("Digite um valor válido.")
        break
    print()
    
    if list(perguntas[2].values())[1][resposta_do_usuario_3] == resposta_certa_pergunta_3:
        print("Você acertou!😄")
        contagem_de_acertos += 1
    else:
        print("Você errou!😓")
        contagem_de_erros += 1
    print()
    
    if contagem_de_acertos >= contagem_de_erros:
        print(f'Parabéns, você acertou {contagem_de_acertos}', 'pergunta' if contagem_de_acertos == 1 else 'perguntas', '✨🎉🎊')# redundante porque 'contagem_de_acertos'
        #vai ser sempre >1 senão vai cair no else
        #('valor' if True else 'Outro valor' if True else 'Fim')
    else:
        print(f'Que pena, você errou {contagem_de_erros}', 'pergunta' if contagem_de_erros == 1 else 'perguntas', '😰😱📚')
    break