from ManejoArchivos import ManejoArchivos

# Manejo de contexto WITH: sintaxis simplificada, abre, cierra el archivo
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
    #print(archivo.read())
# no hace falta el try, ni el finally
# en el contexto WITH lo que se ejecuta de manera automática
# utiliza diferentes métodos: __enter__ este es el que abre
# ahora el siguiente método es el que cierra: __exit__

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())