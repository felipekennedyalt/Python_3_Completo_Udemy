a = 'A'
b =  "B"
c = 1.1
# formato = 'a = {} b = {} c = {}'.format(a, b, c) # ao invez de só depender da ordem também posso pegar pelo indice, começando pelo o zero é claro
string = 'a = {0} a = {0} b = {1} c = {nome3:.2f}' # explicando o erro outo of range, vai acontecer bastante com listas, for, string, quando buscar por algo que já acabou vai dar esse erro
#formato = string.format(a, b, c) # o erro out of range vai acontecer caso eu coloque outra uma quarta chave na variável string, 
                                 # sendo que só está sendo passado 3 valores, argumentos, no método format()
# parametro nomeado no python é quando dou um nome para os argumentos que estou chamando
formato = string.format(a, b, nome3 = c) # e tudo que vier depois de um parametro nomeado precisa ser também nomeado, 
# então se nomear o b e não nomear o c, vai dar erro, e se nomear o primeiro o 'a' vou ter que nomear todo o resto, se não vai dar erro
print(formato)