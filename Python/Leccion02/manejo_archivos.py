# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') # la w es de write que significa escribir
    archivo.write('Programamos con diferentes tipoos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son:\n r read,\n a append,\n w write,\n x crea un archivo\n')
    archivo.write(' t text,\n b binario,\n w+ write and read,\n r+ read and write\n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('con esto terminamos')
except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo
# archivo.write('todo quedo perfecto') es un error no se puede abrir un archivo cerrado "finally"