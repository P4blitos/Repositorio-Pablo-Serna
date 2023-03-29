 class animales{
    
    constructor(nombreA, edadA, sonido){
        this.nombreA=nombreA;
        this.edadA= edadA;
        this.sonido=sonido;
    }
    sonido(){
        console.log(`${this.nombreA} tiene el sonido ${this.sonido}`);
    }
}

 class Gatos extends animales{

    constructor(nombreA, edadA, sonido){
        super(nombreA,edadA, sonido)
        this.jugueteFavorito = {
            tipo: 'bola de goma',
            color: 'rojo'
        }
    }

    jugar() {
        console.log(`${this.nombreA} le encanta jugar con su ${this.jugueteFavorito.color} ${this.jugueteFavorito.tipo}`);
    }

    sonido() {
        console.log(`${this.nombre} hace ${this.sonido}`);
    }
}
export let myGato = new Gatos('Jack',10,'Miauu');

export{animales,Gatos}