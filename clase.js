console.log('Hola mundo');//imprimir en consola
console.log(Math.random());//llamar metodos

//crear variables
let edad=10;
let age =20;
let mensaje= "Hola queridos usuarios";
var mensaje2="Mensaje 2";
console.log(mensaje +' '+ mensaje2);

//mismo dato si suma
console.log(edad+age);
//tamaño
console.log(mensaje2.length);

let Tverdad= true;
let Otro = null;

//existe el "==="verifica sin el mismo tipo de dato y despues el valor

//como crear variables con otro uso y no se deja nunca cambiar su valor
const moneda='COP';
const numeroColumna=4;


//****************************************************************************************************************** */
//funciones
function suma(num1, num2) {
    return num1+num2;
}

//funcion anonima

const hola= function(){
    return 'Hola'
}
//**************************************************************************************************************** */
//funcion de flecha *Mas usado*
const sumar=(num1,num2) =>{
    return num1+num2;
}

let resultado= sumar(3,5);
console.log(resultado);

//si solo hay un aprametro no es necesari parentesis
const multiplicarDos= numero=>{
    return numero*2;
}
//sin parametros
const multiplicarTres =()=>{
    return 3+5;
}
//********************************************************************************************************* */

//Arreglos

let numero=[1,2,6,25 ];

//ingresar uno nuevo
numero.push(7);
console.log(numero)
//sacar el ultimo
numero.pop();
console.log(numero);