var valor = document.getElementById("valor");
valor.addEventListener('keyup', convertir);
txtResultado = document.getElementById("resultado");

unidad1 = document.getElementById("unidad1");
unidad1.addEventListener('change', convertir);

unidad2 = document.getElementById("unidad2");
unidad2.addEventListener('change', convertir);

//Calculamos el resultado acá:
var resultado;

//Función que realizará el cálculo:
function convertir(){
    //En el caso en que no se ingrese ningún valor:
    if(valor.value == ''){
        return;
    }

    //Conversión a número de lo que se tipea:
    numero = valor.value;
    numero = parseFloat(numero);

    if(unidad1.value == "Kilómetro" && unidad2.value == "Kilómetro"){
        resultado = numero * 1;
        txtResultado.innerHTML = numero +" "+"Kilómetro/s equivalen a "+ resultado +" "+" Kilometro/s.";
    }
    if(unidad1.value == "Kilómetro" && unidad2.value == "Metro"){
        resultado = numero * 1000;
        txtResultado.innerHTML = numero +" "+"Kilómetro/s equivalen a "+ resultado +" "+" Metro/s.";
    }
    if(unidad1.value == "Kilómetro" && unidad2.value == "Centímetro"){
        resultado = numero * 10000;
        txtResultado.innerHTML = numero +" "+"Kilómetro/s equivalen a "+ resultado +" "+" Centímetro/s.";
    }
    
    
    if(unidad1.value == "Metro" && unidad2.value == "Kilómetro"){
        resultado = numero / 1000;
        txtResultado.innerHTML = numero +" "+"Metro/s equivalen a "+ resultado + " "+"Kilometro/s.";
    }
    if(unidad1.value == "Metro" && unidad2.value == "Metro"){
        resultado = numero * 1;
        txtResultado.innerHTML = numero +" "+"Metro/s equivalen a "+ resultado +" "+" Metro/s.";
    }
    if(unidad1.value == "Metro" && unidad2.value == "Centímetro"){
        resultado = numero * 100;
        txtResultado.innerHTML = numero +" "+"Metro/s equivalen a "+ resultado +" "+" Centímetro/s.";
    }


    if(unidad1.value == "Centímetro" && unidad2.value == "Kilómetro"){
        resultado = numero / 100000;
        txtResultado.innerHTML = numero +" "+"Centímetro/s equivalen a "+resultado + " "+ "Kilometro/s.";
    }
    if(unidad1.value == "Centímetro" && unidad2.value == "Metro"){
        resultado = numero / 100;
        txtResultado.innerHTML = numero+" "+"Centímetro/s equivalen a "+resultado+" "+"Metro/s.";
    }
    if(unidad1.value == "Centímetro" && unidad2.value == "Centímetro"){
        resultado = numero * 1;
        txtResultado.innerHTML = numero+" "+"Centímetro/s equivalen a "+resultado+" "+"Centímetro/s.";
    }
}
