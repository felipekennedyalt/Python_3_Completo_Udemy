frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'
        
frase_2 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dignissim dolor sed eros rutrum, nec malesuada elit auctor. Nulla vitae fermentum mi, feugiat pulvinar neque. Mauris turpis nisi, convallis nec consectetur ut, aliquet a enim. Praesent in nunc ac velit convallis tristique. Fusce volutpat venenatis dolor, id porta lectus mattis non. Aliquam neque odio, pretium fermentum odio in, venenatis maximus nibh. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse ac sapien tincidunt, gravida mauris ut, lacinia sapien. Aenean nec lacus ac libero congue ultrices eget vitae mi. Nullam aliquam tincidunt sem, nec tempus ex molestie sit amet. Donec id magna ipsum. Suspendisse sollicitudin porta tellus in eleifend. Morbi vitae ipsum a tellus porttitor mattis quis in turpis. Etiam tincidunt leo eget placerat finibus. Nunc diam magna, egestas ut diam at, sagittis facilisis risus. Quisque id euismod arcu, et ullamcorper elit.

"""
        
print(frase.count('python'))# método count() só funciona com strings e conta quantas vezes uma palavra que você coloca nométodo ou uma frase aparece em uma string, letras maiúsculas e minúsculas fazem diferença.

palavra_que_o_usuario_procura = input("Digite qual palavra você procura: ")
print(f'A palavra que você procura é {palavra_que_o_usuario_procura}, ela aparece {frase.count(palavra_que_o_usuario_procura)} vezes na frase 1, e na frase 2 foram {frase_2.count(palavra_que_o_usuario_procura)}')

i = 0 
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu and letra_atual != ' ': # tirando o espaço que aparece 14 vezes
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_que_apareceu_mais_vezes = letra_atual
    
    
    print(f" {letra_atual} apareceu {quantas_vezes_letra_apareceu} vezes na frase")
    print(letra_atual)
    
    i += 1
print(f"A letra que aprareceu mais vezes foi ({letra_que_apareceu_mais_vezes}) ela apareceu {qtd_apareceu_mais_vezes}")