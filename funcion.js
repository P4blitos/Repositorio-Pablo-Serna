let nombre= 'Pablo Andres Serna'

const saludar = () =>{
    return console.log("Hola como estas");
}

saludar();

const saludarNom = nombre =>{
     console.log("Hola como estas"+' '+ nombre);
}

saludarNom(nombre);

const mayor = (num1,num2)=>{
    let mayo=null;
    if (num1 > num2) {
        mayo=num1;
    }
    else if(num2 > num1){
        mayo=num2;
    }
    else {
        console.log("Son iguales");
    }
    return mayo;
}

let resul= mayor(3,5)
console.log(resul);