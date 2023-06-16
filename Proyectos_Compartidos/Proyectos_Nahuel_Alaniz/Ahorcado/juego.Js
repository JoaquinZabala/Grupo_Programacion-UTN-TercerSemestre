// Definir la palabra a adivinar
var palabraAdivinar = prompt("Jugador 1: Ingresa la palabra a adivinar").toUpperCase();

// Inicializar el estado del juego
var letrasAdivinadas = [];
var intentosRestantes = 6;

// Función para dibujar el muñeco ahorcado
function dibujarAhorcado() {
  var partesAhorcado = ["cabeza", "cuerpo", "brazo-izquierdo", "brazo-derecho", "pierna-izquierda", "pierna-derecha"];
  var partesRestantes = partesAhorcado.slice(0, partesAhorcado.length - intentosRestantes);
  
  partesRestantes.forEach(function (parte) {
    document.getElementById(parte).style.backgroundColor = "black";
  });
}

// Función para actualizar la palabra a mostrar
function actualizarPalabraMostrada() {
  var palabraMostrada = "";
  
  for (var i = 0; i < palabraAdivinar.length; i++) {
    if (letrasAdivinadas.includes(palabraAdivinar[i])) {
      palabraMostrada += palabraAdivinar[i];
    } else {
      palabraMostrada += "_";
    }
    palabraMostrada += " ";
  }
  
  document.getElementById("palabra").textContent = palabraMostrada;
}

// Función para manejar los intentos de adivinar una letra
function adivinar() {
  var letraInput = document.getElementById("adivinar-input").value.toUpperCase();
  
  if (letraInput.length !== 1) {
    alert("Ingresa una sola letra.");
    return;
  }
  
  if (letrasAdivinadas.includes(letraInput)) {
    alert("Ya has adivinado esa letra.");
    return;
  }
  
  letrasAdivinadas.push(letraInput);
  
  if (palabraAdivinar.includes(letraInput)) {
    actualizarPalabraMostrada();
    if (!document.getElementById("palabra").textContent.includes("_")) {
      alert("¡Has ganado! La palabra era: " + palabraAdivinar);
    }
  } else {
    intentosRestantes--;
    dibujarAhorcado();
    
    if (intentosRestantes === 0) {
      alert("¡Has perdido! La palabra era: " + palabraAdivinar);
    } else {
      document.getElementById("intentos").textContent = "Intentos restantes: " + intentosRestantes;
    }
  }
  
  document.getElementById("adivinar-input").value = "";
}

// Inicializar el juego
actualizarPalabraMostrada();
document.getElementById("intentos").textContent = "Intentos restantes: " + intentosRestantes;

