"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

# print('valor' if True else 'Outro valor')

# condicao = 10 == 10
# variavel = 'valor' if condicao else 'outro valor'
# print(variavel)

# digito = 10
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito # mesma coisa da condição de cima, só de uma jeito diferente
# print(novo_digito)

print('valor' if True else 'Outro valor' if True else 'Fim')# não é muito bom fazer assim