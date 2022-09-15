import math
x = int(input('digite um número:'))
raiz = math.sqrt(x)
print(f'a raiz quadrada de {x} é {raiz:.1f}')


# Outra forma de fazer 

from math import sqrt,ceil
x = int(input('digite um número:'))
raiz = sqrt(x)
print(f'a raiz quadrada de {x} é {ceil(raiz):.2f}')