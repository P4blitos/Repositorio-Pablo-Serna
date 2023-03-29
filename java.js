import {despedir, suma} from './modulo2.js';

const saludar = (nombre, apellido)=> {
    return `Hola ${nombre} ${apellido}`
}

console.log(saludar('raul', 'ospina'));
let chao = despedir('Pablo', 'Serna')
console.log(chao);
console.log(suma(2,5));