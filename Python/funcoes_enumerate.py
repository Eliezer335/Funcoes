## Retorna o indice de uma coleção de dados 


animais = ["cachorro","gato","elefante","papagaio"]

print(list(enumerate(animais)))

## Iterar uma lista com enumerate

for i,valor in enumerate(animais):
    if i > 1:
        break
    else:
        print(valor)

