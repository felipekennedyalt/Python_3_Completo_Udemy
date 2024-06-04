"""
Iterando strings com while
"""
#-------0123456789
nome = 'Felipe Kennedy' #Iteráveis
# bojetivo F*e*l*i*p*e* K*e*n*n*e*d*y*
# how do i make the variable name become like this F*e*l*i*p*e* K*e*n*n*e*d*y* using while?

tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < tamanho_nome:
    
    letra = nome[indice]
    novo_nome += letra + '*' # novo nome = novo_nome + letra + '*'. aqui nome[indice] ta pegando as letra de uma por uma e passando pra novo_nome onde eu estou adicionando o * depois das letras que a variavel letra entrega para novo_nome (também da pra fazer assim ) novo_nome += f'*{letra}' mas vai falta um * no final do mesmo jeito que o neu falta um * no começo
    indice += 1

print(f"Seu nome ficou {novo_nome}")