# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alternar
# Funções decoradoras são funções que decoram outras funções
# Decoradoras são usadas para fazer o Python
# Usar as funções decoradoras em outras funções

def inverte_string(string):
    return string[::-1]

def criar_funcao(func): # Essa função é a decoradora
    def interna(*args, **kwargs):
        print('vou te decorar')
        resultado = func(*args, **kwargs)
        for arg in args:
            e_string(arg)
        print(f'o seu resultado foi: {resultado}.')
        print('você foi decorado')
        return resultado
    return interna

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = 'Felipe Kennedy'

print(inverte_string(invertida))

inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida_2 = inverte_string_checando_parametro('123')

print(invertida_2)