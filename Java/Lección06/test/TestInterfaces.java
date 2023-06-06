/*
Clase de para prueba 
 */
package test;

import accesodatos.*;


public class TestInterfaces {
    public static void main(String[] args) {
    // no puede ser instanciada la interface, por lo que usamos una de las clases
        IAccesoDatos datos = new ImplementacionMySql();
        //Si damos click sobre listar y damos a Ctrl, volvemos a dar click nos lleva a la interface
        //datos.listar();
        
       // imprimir(datos);
        
        datos = new ImplemantacionOracle();
        //datos.listar();
        
        imprimir(datos);
    }
 public static void imprimir(IAccesoDatos datos){
     datos.listar();
 }
}

  
