"""
https://docs.python.org/pt-br/3/library/stdtypes.html
imutaveis que vimos: str, int,float,bool
"""
string = 'Felipe'
#string[4] = 'ABC' (não sá pois é imutavel)
outra_variavel = f'{string[:4]}ABC{string[5:]}'

print(string[4])
print(outra_variavel.zfill(100))