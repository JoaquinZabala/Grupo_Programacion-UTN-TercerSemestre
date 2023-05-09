
package test;

import domain.*;


public class TestSobreescritura {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan",10000);
        imprimir(empleado1);
       // System.out.println("emplado1= "+empleado1.obtenerDetalles());
         empleado1 = new Gerente("José", 5000,"Sistemas");
         imprimir(empleado1);
       // Gerente gerente1 = new Gerente("José", 5000,"Sistemas");
       //imprimir(gerente1);
       // System.out.println("gerente1 = "+gerente1.obtenerDetalles());
    }
    
   public static void imprimir(Empleado empleado){
       String detalles =empleado.obtenerDetalles();
       //System.out.println("empleado = "+empleado.obtenerDetalles());
       System.out.println("detalles= "+detalles);
   }
    
    
}
