"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5
qtd_execuções = 0
linha = 1

while linha <= qtd_linhas:
    
    coluna = 1
    print("--------------" ,linha)
    linha += 1
    while coluna <= qtd_colunas:
        print("I", coluna)
        coluna += 1
        qtd_execuções += 1
    
# while linha <= qtd_linhas:
#     coluna = 1
#     linha += 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
        
    
print(f"esse código foi executado {qtd_execuções} vezes")
print('Acabou')