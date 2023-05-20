let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma:'es',
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas en mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){//metodo o funcion en JavaScript
        return this.nombre+' '+this.apellido;     
    },

get nombreEdad(){ //Este es el metodo get
     return 'El nombre es: '+this.nombre+', Edad: '+this.edad;

}
    
}
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona)
console.log(persona.nombreCompleto())
console.log('Ejecutando con un objeto');
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salida 14';
persona2.telefono = '2604889922';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']); //Accedemos como si fuera un arreglo
console.log('Usamos elciclo for in')
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);    
}
console.log('cambiamos y eliminamosun error')
persona.apellida = 'Contreras'; // Cambiamos dinamicamente un valor del objeto
delete persona.apellida;//Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distinta formas de imprimir un objeto:forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Numero 2 : A traves del ciclo for in 
console.log('Distinta formas de imprimir un objet: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Object.values()
console.log('Distinta forma de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log('Distinta forma de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set  para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){//constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo','Lopez','lopez@gmail.com');
padre.nombre = 'Luis'; //modificado el nombre
console.log(padre);
console.log(padre.nombreCompleto());//Utilizamos la funcion
let madre = new Persona3('Laura','Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.nombreCompleto());