
class animales{
    
    constructor(nombreA, edadA, sonido){
        this.nombreA=nombreA;
        this.edadA= edadA;
        this.sonido
    }
    sonido(){
        return `${this.nombreA} tiene el sonido ${this.sonido}`;
    }
}

class Gatos extends animales{

    constructor(nombreA, edadA, sonido,caza){
        super(nombreA,edadA, sonido)
        this.caza = caza;
    }

    maullar(){
        return `yo puedo hacer el sonido ${this.sonido}`;
    }
}
