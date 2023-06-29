package UTN;

import UTN.conexión.Conexión;

public class Main {
    public static void main(String[] args) {
       var conexión = conexión.getConnection()
               if(conexión != null){
                   System.out.println("conexión exitosa: "+conexión);
               else
                   System.out.println("Error al conectarse");
    }//Fin main
}//Fin clase