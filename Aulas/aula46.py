for i in range(10):# aqui to pasando o intervalo que é de 0 a 9, o 10 não é incluido
    if i == 2:
        print('seu i é 2, pulando...')
        continue# continue faz voltar pro inicio do loop imediatamente
    
    if i == 8:
        print('seu i é 8, seu else não executará.')
        break# break faz pular pra saida do loop imediatamente
    for j in range(1, 3):#aqui estou dizendo que o intervalo começa em 1 e termina em 2, o 3 não entra é como se fosse < 3
        print(i,j)
else:
    print('For completo com sucesso.')