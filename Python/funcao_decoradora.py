#funcoes decoradoras potenciaiza ou modificao a logica de outra funçao ou metodo

#Uma funçao decoradora e quando ultilizamos o @ em cima de uma funçao

#exemplo 

#@decoradora 
#def oi():
# print('oi)

## Criar uma funçao decoradora 

def master(msg):
    def imprime():
        print("esse e a funçao decoradora")
    msg()
    return imprime

##criar uma funçao que vai receber a decoradora
@master
def chama_funcao():
    print("esta chamando a funçao real ")

#chama a funçao
    
chama_funcao()