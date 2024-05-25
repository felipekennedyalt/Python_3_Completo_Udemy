"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(caractere)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - força o numero a aparecer antes do dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:$^10}.')
print(f'{variavel:-^10}.')
print(f'{-1000.00616499463:,.1f}')
print(f'{1000.00616499463:+,.1f}')
print(f'{1000.00616499463:0>+10,.1f}')
print(f'{1000.00616499463:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')