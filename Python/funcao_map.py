## A função map temcomo objetivo aplicar a funçao ou uma açao em todos os elementos
#de uma estrutura de dados retornado uma noova sequencia ou resultado

import math

lista = [1,2,3,44,55]

def soma(x):
    return x+2

print(list(map(soma,lista)))

print(list(map(math.sqrt,lista)))