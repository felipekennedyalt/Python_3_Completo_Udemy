# generator expression, Iterables e Iterators em Python

import pprint

def p(valor):
    pprint.pprint(valor)

iterable = ['Eu', 'Tenho', '__iter__'] 
iterator = iterable.__iter__() #ou iter(iterable) # tem __iter__ e __next__ #Iterator não sabe nada sobre o iterável, só sabe entregar o proximo valor e o resto que se foda

p(next(iterator))
p(next(iterator))# o iterator esgota os valores, se eu pedir o primeiro, ou valores anteriores ele não vai saber me dar, entao se eu chamar o iterator em um 'for' e ele acabar, se eu chama-lo em outro 'for' ele ja vai estar no ultimo valor. ou seja, não podemos fazer mais de um 'for' em um mesmo iterator, por isso podemos converte-lo em lista antes de usar.
p(next(iterator))# se colocar mais um vai dar a exeção 'StopIteration', pois não vai mais ter valores para mostrar