## e uma funçao que retorna sequencia de elementos em formato de tuplas 

dicverduras = {1:"cebola", 2:"alface", 3:"repolho", 4:"beterraba"}

dicfrutas = {1:"maça",2:"laranja",3:"pera"}

print(list(zip(dicverduras.items(),dicfrutas.items())))