class Producto {
    static contadorProductos = 0;
    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;
        this.nombre = nombre;
        this.precio = precio;
    }
    get idProducto() {
        return this._idProducto;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get precio() {
        return this._precio;
    }
    set precio(precio) {
        this._precio = precio;
    }
    toString() { //Template Literals: Nos permite insertar codigo dinamicamente 
        return ` idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}`;
    }
} //Fin de la clase Producto

class Orden extends Producto{
    static contadorProductosAgregados = 0;
    static get MAX_PRODUCTOS (){
        return 5; //Simula una constante
    };
    constructor(){
        super();    
        this._idOrden = ++Orden.contadorProductosAgregados;
        this._productos = [];
        this._contadorProductosAgregados = 0;
        if  (Orden.contadorProductosAgregados > Orden.MAX_PRODUCTOS){
            console.log("No se pueden agregar más productos");
        }

    }
    get idOrden(){
        return this._idOrden;
    }
    agregarProducto(producto){
        if(this._productos.length < Orden.MAX_PRODUCTOS){
            this._productos.push(producto); //Tenemos 2 tipos de sintaxis: 1
            //this._producto[this._contadorProductosAgregados++] = producto; //Segunda sintaxis
        }else{
            console.log("No se pueden agregar más productos");
        }
    } //Fin del metodo agregarProducto
    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
        } //Fin ciclo for
        return totalVenta;
    } //Fin del metodo calcular total
    mostrarOrden(){
        let productosOrden = "";
        for(let producto of this._productos){
            productosOrden += '\n{'+producto.toString() + '}';
        } //Fin del ciclo for
        console.log( `Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productosOrden}, Cantidad de productos: ${this._productos.length}`);
    }//Fin de la clase orden
}
//Agregando productos

let producto1 = new Producto('Pantalon', 200);
let producto2 = new Producto('Camisa', 150);
let producto3 = new Producto('Cinturon', 100);
let producto4 = new Producto('Remera', 50);
let producto5 = new Producto('Zapatillas', 500);
let producto6 = new Producto('Gorra', 200);


//New orden

let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto4);
orden1.agregarProducto(producto5);
orden1.agregarProducto(producto6);

//mostrando orden
orden1.mostrarOrden();