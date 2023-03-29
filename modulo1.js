import {Animales, Gatos,myGato} from './modulo2.js';

const conocerMascotas = () => {
    let miGato = new Gatos('Tom', 2,'Miauuu');
    myGato.edadA= 3;
    miGato.jugueteFavorito.color="Dorado";
    
    myGato.jugar();
    
    miGato.jugar();
    
  };
  
conocerMascotas();