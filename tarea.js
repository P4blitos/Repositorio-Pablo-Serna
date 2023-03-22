//1 Punto

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
    
}