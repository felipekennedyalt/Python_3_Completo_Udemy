#manipulando chaves e valores em dicionários
pessoa = {
    'nome': 'Felipe', # dentro do dicionário se usa ':' e não o sinal de igual '=', mas se eu fizer usando a função dict(), então é com '=' ex.: pessoa = dict(nome='felipe', idade=18)
    'sobrenome': 'Kennedy',
    'idade': 28,
    'altura': 1.69,
    'endereços':[
        {'rua': 'Rua 1', 'numero': 123},# aqui tenho uma lista com vários dicionarios dentro registrando o endereço
        {'rua': 'Rua 2', 'numero': 456},
    ]
}

#criar nova chave no meu dicionário existente
pessoa['peso'] = 70 #criei uma nova chave chamada 'peso'
chave = 'sexo' # dá pra ser mais dinâmico, usando vairáveis

pessoa[chave] = 'Masculino'

#pessoa['peso'] = 90 #se eu quiser mudar o valor
del pessoa['peso'] #como deletar uma chave, se eu deletar 'peso' vai dar keyerror, pois o print(pessoa['peso']), não vai conseguir pegar 'peso' por não existir mais

# if pessoa['peso']:# não da certo, pois o if não para exceção
#     print(pessoa['peso'])

#mas da pra usar um metodo dentro do dicionario chamado get()
# if pessoa.get('peso', 'não existe'): # get() tenta obter uma chave, por padrão ele retorna 'None' se a chave não existir.
#     print('oi')

print(pessoa.get('peso', 'não há a chave peso'))# por padrão o get vai retornar um valor 'None' caso a chave não exista. mas podemos mudar esse valor assim 'pessoa.get('peso', 'novo valor')'
if pessoa.get('peso') is not None:# a chave peso continua sem existir, essa função get() só retornou o que eu pedi, não adicionou valor à chave que não existia.
    print(pessoa['peso'])
else:
    print('não há a chave peso aqui no IF')

#print(pessoa['peso'])# erro keyerror é quando a chave não existe no dicionário
print(pessoa[chave])# dá pra ser mais dinâmico, usando vairáveis