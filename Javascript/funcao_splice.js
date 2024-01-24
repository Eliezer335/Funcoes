
// afunçao splice ela altera um array pode remover elementos e pode substituir elementos 

//remover 1 elemento apartir da posiçao do indici de memoria

let numeros = [1,2,3,4,5]

numeros.splice(2,1)

console.log("slice " + numeros)

let numeros2 = [1,2,3,4,5]

numeros2.splice(2,1,500)

console.log("Splice2 "+numeros2)