import aula99_package
import aula99_package.modulo_b
# esse arquivo "__init_.py" é executado assim que o módulo for importado.

# engana o python fazendo ele achar qeu tem metodo no package.
print(aula99_package.dobra(4))
print(aula99_package.soma_do_modulo(2, 5))

# se eu usar o f2 no fala oi vai mudar tanto aqui quando na classe onde o metodo está, pois o vscode entende onde esse metodo está sendo usado
aula99_package.modulo_b.fala_oi()
#O init pode ser usado para fazer o python achar que o package é um modulo importando as coisas desse package como se fosse um módulo.