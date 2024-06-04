"""
Repetições
wilhe (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Digite o nome: ').lower()
    print(f'O nome que você digitou é {nome}')
    if nome == 'sair':
        break # sai do laço
    
print('Acabou')