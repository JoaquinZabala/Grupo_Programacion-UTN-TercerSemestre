package mundopc;

import ar.com.system2023.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP",13);// importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth","HP");
        Raton ratonHP = new Raton("Bluetooth","HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        //Creación de objetos de diferente marca
        Monitor monitorGamer = new Monitor("Gamer",32);
        Teclado tecladoGamer = new Teclado("Bluetooth","Gamer");
        Raton ratonGamer = new Raton("Bluetooth","Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        Computadora computadorasVarias = new Computadora("Computadoras varias", monitorHP, tecladoGamer, ratonHP);
        
        Monitor monitorGenius = new Monitor("Genius",17);
        Teclado tecladoGenius = new Teclado("Bluetooth","Genius");
        Raton ratonGenius = new Raton("Bluetooth","Genius");
        Computadora computadoraGenius = new Computadora("Computadora Genius", monitorGenius, tecladoGenius, ratonGenius);
        
        Monitor monitorPositivoBGH = new Monitor("PositivoBGH",15);
        Teclado tecladoPositivoBGH = new Teclado("Bluetooth","PositivoBGH");
        Raton ratonPositivoBGH = new Raton("Bluetooth","PositivoBGH");
        Computadora computadoraPositivoBGH = new Computadora("Computadora PositivoBGH", monitorPositivoBGH, tecladoPositivoBGH, ratonPositivoBGH);
        
        Monitor monitorStandar = new Monitor("Standar",21);
        Teclado tecladoStandar = new Teclado("Bluetooth","Standar");
        Raton ratonStandar = new Raton("Bluetooth","Standar");
        Computadora computadoraStandar = new Computadora("Computadora Standar", monitorStandar, tecladoStandar, ratonStandar);
        
        Monitor monitorLG = new Monitor("LG",18);
        Teclado tecladoLG = new Teclado("Bluetooth","LG");
        Raton ratonLG = new Raton("Bluetooth","LG");
        Computadora computadoraLG = new Computadora("Computadora LG", monitorLG, tecladoLG, ratonLG);
        
        Monitor monitorStart = new Monitor("LG",23);
        Teclado tecladoStart = new Teclado("Bluetooth","LG");
        Raton ratonStart = new Raton("Bluetooth","Start");
        Computadora computadoraStart = new Computadora("Computadora Start", monitorLG, tecladoHP, ratonStart);
        
        Monitor monitorIntel = new Monitor("Intel",32);
        Teclado tecladoIntel = new Teclado("Bluetooth","Intel");
        Raton ratonIntel = new Raton("Bluetooth","Intel");
        Computadora computadoraIntel = new Computadora("Computadora Intel", monitorIntel, tecladoIntel, ratonIntel);
        
        Monitor monitorSamsung = new Monitor("Samsung",18);
        Teclado tecladoSamsung = new Teclado("Bluetooth","Samsung");
        Raton ratonSamsung = new Raton("Bluetooth","Samsung");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung", monitorSamsung, tecladoSamsung, ratonSamsung);
        
        Monitor monitorXview = new Monitor("xview",22);
        Teclado tecladoXview = new Teclado("Bluetooth","Xview");
        Raton ratonXview = new Raton("Bluetooth","Xview");
        Computadora computadoraXview = new Computadora("Computadora Xview", monitorXview, tecladoXview, ratonXview);
        
        Orden orden1 = new Orden();//Inicializamos el arreglo vacio
        Orden orden2 = new Orden();//una lista nueva para el objeto 2
        Orden orden3 = new Orden();
        Orden orden4 = new Orden();
        Orden orden5 = new Orden();
        Orden orden6 = new Orden();
        Orden orden7 = new Orden();
        Orden orden8 = new Orden();
        Orden orden9 = new Orden();
        Orden orden10 = new Orden();
        
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden2.agregarComputadora(computadoraHP);
        orden3.agregarComputadora(computadoraGenius);
        orden4.agregarComputadora(computadoraPositivoBGH);
        orden5.agregarComputadora(computadoraStandar);
        orden6.agregarComputadora(computadoraLG);
        orden7.agregarComputadora(computadoraStart);
        orden8.agregarComputadora(computadoraIntel);
        orden9.agregarComputadora(computadoraSamsung);
        orden10.agregarComputadora(computadoraXview);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();
        orden4.mostrarOrden();
        orden5.mostrarOrden();
        orden6.mostrarOrden();
        orden7.mostrarOrden();
        orden8.mostrarOrden();
        orden9.mostrarOrden();
        orden10.mostrarOrden(); 
    }
}
