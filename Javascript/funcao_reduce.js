
let numeros = [1,2,3,4,5]

// a funçao ira somar todos os elementos do array resultando apenas um valor 

let somaTotal = numeros.reduce(function(x,y){
    return x+y
})

//console.log("soma dos elementos "+ somaTotal)