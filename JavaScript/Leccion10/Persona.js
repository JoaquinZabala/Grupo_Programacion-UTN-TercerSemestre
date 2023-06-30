class Persona{
    static contadorPersona = 0;
    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }
    get idPersona(){
        return this._idPersonas;
    }
    get nombre(nombre){
        this._nombre = nombre;
    
    }
    get apellido(apellido){
        return this._apellido;
    
    
    }
    get edad(edad){
        this._edad = edad;
    }
    toString(){
        return
         ${this._idPersonas}
        ${this._nombre}
        ${this._apellido}
        ${this._edad};
        
    }
}