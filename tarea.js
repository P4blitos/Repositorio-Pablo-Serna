//Punto 1
const juegos={
    nombre: 'Dark Souls',
    fecha_lanzamiento: 2011 ,
    Productora: 'FromSoftware',
    director: 'Hidetaka Miyazaki',
    caracteristicas:{
        Precio: 200000,
        Consola: 'Ps3 / PC',
        Idioma: 'multi-lenguage',
        Genero: 'aRPG'
    },
    //metodo
    iniciar:function(){
        return `Inicio el juego:  ${this.nombre} de la  productora ${this.Productora}`
    },

    salir:function(){
        return`${this.director} te agradece por jugar nuestro juego de tipo ${this.caracteristicas.Genero}`
    }
}

console.log(juegos.iniciar())
console.log(juegos.salir())

//Punto 2

class vehiculo{
    constructor(nombre,marca, color, modelo){
        this.nombre=nombre;
        this.marca=marca;
        this.color=color;
        this.modelo=modelo;
    }
    
}

class moto extends vehiculo{
    constructor(nombre, marca, color, modelo, canLlantas){
        super(nombre,marca, color, modelo);
        this.canLlantas=canLlantas;
    }
    mostrar(){
        return `Est@ ${this.nombre}  de marca ${this.marca} tiene ${this.canLlantas} llantas`;
    }
}

let vehiculito = new moto('Moto','AKT','Rojo',2020,2);
console.log(vehiculito.mostrar());

//punto 3
const cambiar = (objeto) => {
    vehiculito.marca='Toyota';
    vehiculito.color='Azul';
    vehiculito.modelo=2019;
    vehiculito.canLlantas=3;
    return vehiculito;
}

console.log(cambiar(vehiculito));
console.log(cambiar(vehiculito).mostrar());