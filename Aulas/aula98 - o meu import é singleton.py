import importlib # bliblioteca de importação que posso usar para recarregar o import
import aula98_m_ # o meu import é singleton, significa que só pode existir uma instância dele enquanto eu estou executando

print(aula98_m_.nome)

for i in range(10):
    print(i)
    #import aula98_m_
    importlib.reload(aula98_m_)
print('fim')