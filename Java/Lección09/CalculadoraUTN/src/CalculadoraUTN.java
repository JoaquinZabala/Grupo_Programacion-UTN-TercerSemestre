import java.util.Scanner;
public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true) {//Ciclo infinito
            System.out.println("******* Aplicaion Calculadora *******");
            mostrarMenu();

            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    ejecutarOperacion(operacion,entrada);
                }//Fin del If
                else if (operacion == 5) {
                    System.out.println("Hasta pronto....");
                    break;//Rompe el ciclo y sale
                }//Fin else if
                else {
                    System.out.println("Opcion erronea : " + operacion);
                } //Fin else   System.out.println("****** Aplicacion Calculadora *******");
                //Imprimimos un salto de linea antes de repetir el menú
                System.out.println();
            }catch (Exception e){//Fin try comienzo del catch
                System.out.println("Ocurrio un error " + e.getMessage());
                System.out.println();
            }//Fin del catch

        }//Fin while
    }//Fin main
    private static void mostrarMenu(){
        //Mostramos el menú
        System.out.println("""
                    1-Suma
                    2-Resta
                    3-Multiplicación
                    4-Division
                    5-Salir
                    """);

        System.out.println("Operacion a realizar? ");
    }//Fin metodo mostrarMenu

    private static void ejecutarOperacion(int operacion,Scanner entrada){
        System.out.println("Digite el valor para el operando1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.println("Digite el valor para el operando2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        double resultado;
        switch (operacion) {
            case 1 -> { //Suma
                resultado = operando1 + operando2;
                System.out.println("El resultado de la suma : " + resultado);
            }
            case 2 -> {//Resta
                resultado = operando1 - operando2;
                System.out.println("El resultado de la resta : " + resultado);
            }
            case 3 -> { //Multilicación
                resultado = operando1 * operando2;
                System.out.println("El resultado de la multiplicación : " + resultado);
            }
            case 4 -> {//División
                resultado = operando1 / operando2;
                System.out.println("El resultado de la división : " + resultado);
            }
            default -> System.out.println("Opción es erronea " + operacion);
        }//Fin switch
    }//Fin metodo ejecutarOperacion
}//Fin clase
