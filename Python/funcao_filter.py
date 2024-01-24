##Funçao filter filtra elementos de uma estrutura de dados 
# e fitra o valor que queremos encontrar 

listamista = [ 1,"João","Pedro",53]

def busca(x):
    return x == "João"

#nao otimizada
print(list(filter(busca,listamista)))

#Forma otimizada
print(list(filter(lambda x: x == "Pedro",listamista)))

