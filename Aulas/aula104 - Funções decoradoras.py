# Funções decoradoras e decoradores
# Decorar = adicionar/remover/restringir/alterar funcionalidades a uma função já existente
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
# Decoradores são "syntax sugar" (açúcar sintático) para funções decoradoras.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print("O seu resultado é: ", resultado)
        print('Ok, agora você está decorado!')
        return resultado
    return interna

@criar_funcao #essa é a sintaxe de decorador("syntax sugar"), é o mesmo que fazer: inverte_string_checando_parametro = criar_funcao(inverte_string)
def inverte_string(string):
    print(f"O nome da função é: {inverte_string.__name__}")
    return string[::-1]

def e_string(valor):
    if not isinstance(valor, str):
        raise TypeError(f'O valor {valor} não é uma string!')
    

invertida = inverte_string('123')
print(invertida)

"""inverte_string_checando_parametro = criar_funcao(inverte_string) #era assim do modo anterior
invertida = inverte_string_checando_parametro('123')
print(invertida)"""