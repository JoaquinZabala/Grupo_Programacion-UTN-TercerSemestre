
package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
       // System.out.println("Día 1: "+Dias.JUEVES);
        //indicarDiaSemana(Dias.JUEVES); //LAS ENUMERACIONES SE TRATAN COMO CADENAS
        //no se utiliza comillas, se accede a traves de el operador de punto
        System.out.println("Continente N° 4: "+Continentes.AMERICA);
        System.out.println("N° de paises en el 4to continente: "+Continentes.AMERICA.getPaises());
         System.out.println("N° de habitantes en el 4to continente: "+Continentes.AMERICA.getHabitantes());
        
    }
    private static void indicarDiaSemana(Dias dias){
    switch(dias){
        case LUNES:
            System.out.println("Primer dia de la semana");
            break;
        case MARTES:
            System.out.println("Segundo dia de la semana");
            break;
        case MIERCOLES:
            System.out.println("Tercer dia de la semana");
            break;
        case JUEVES:
            System.out.println("Cuarto dia de la semana");
            break;
        case VIERNES:
             System.out.println("Quinto dia de la semana");
            break;
        case SABADO:
            System.out.println("Sexto dia de la semana");
            break;
        case DOMINGO:
            System.out.println("Septimo dia de la semana");
            break;
        default:
            System.out.println("No se introdujo un dia de la semana");
    }
    }
}
