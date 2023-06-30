class Cliente extends Persona{
    static contadorCliente = 0;

    constructor(nombre, apellido, edad, fecharegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorCliente;
        this._fechaRegistro= fecharegistro;

    }

    get id Cliente(){
        return this._idCliente
    }

    get fecharegistro(){
        return this._(fecharegistro){
            this._fechaRegistro = fecharegistro;
        }

        toString(){
            return 
            ${super.toString()}
            ${this._idCliente} 
            ${this._fechaRegistro}`;

    
    }
}

