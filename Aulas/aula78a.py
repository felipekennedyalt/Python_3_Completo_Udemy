# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# s1 = {1,2,3,3,3,3,1}
l1 = [1,2,3,3,3,3,1]
#quero remover os numeros repetidos dessa lista
s1 = set(l1) # a estrutura set automaticamente remove valores duplicados, mas não garante a ordem, enão os valores podem ficar fora de ordem
l2 = list(s1)
s2 = set('Felipe')
# s3 = {'felipe', 3, 3, 4, 5, ['12']} # set não aceita tipos de valores mutáveis dentro dele, somente imutáveis
s3 = {'felipe', 3, 3, 4, 5, ('12',)} # set não aceita tipos de valores mutáveis dentro dele, somente imutáveis, a tupla é aceita mas precisa da virgula no final, não sei porque, mas foi o que o professor disse
print(l2)
print(s2)
print(s3)
print(3 not in s3)
for numero in s3:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos