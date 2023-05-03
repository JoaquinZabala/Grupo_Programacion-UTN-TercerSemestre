from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar las Peliculas')
        print('3. Eliminar catalogo de Peliculas')
        print('4. Salir')
        opcion = int(input('Ingrese una opción de menú (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_peliculas(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error de tipo: {e}')
        opcion = None
    else:
       print('Salimos del Programa')
