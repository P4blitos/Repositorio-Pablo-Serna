//Callback
const multiplicar = (num1, num2)=>{
    return num1*num2;
}

const validar = (num1, num2, CallbackFn)=>{
    const res = CallbackFn(num1,num2)
    console.log("El resultado de multiplicacion es: "+ res);
}

validar(9,8,multiplicar)

//metodo con arreglo

let edad = [ 12, 20 , 21, 49];

const AñosDespues = edad.map(edades => {
    return " el doble de edad es" + (edades *2) 
})
console.log(AñosDespues)