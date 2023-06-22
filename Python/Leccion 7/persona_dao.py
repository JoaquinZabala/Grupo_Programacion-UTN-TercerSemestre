


class PersonaDAO:
    """
    DAO significa: data Acces Object
    CRUD significa:
                    Create ->Insertar
                    Read -> Seleccionar
                    Update -> Actualizar
                    Delete -> Eliminar
"""
_SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona')
_INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
_ACTUALIZAR = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
_ELIMINAR = 'DELEET FROM persona WHERE id_persona=%s'



#Definimos los metodos de clase 
@classmethod
def seleccionar(cls):
    with Conexion.obtenerConexion():
        with conexion.obtenerCursor() as cursor:
            cursor.excute(cl._SELECCIONAR)
            registro = cursor.fetchall()
            persona = [] #creamos una lista
            for registro in regitros:
                persona = Persona(registros [0], registros[1], registro[2], registro[3])
                persona.append (persona)
            return personas

@classmethod
def insertar (cls,persona):
    with Conexion.obtenerConexion():
        with Conexion.obtenerCursor() as cursor:
            valores= (persona.nombre, persona, apellido, persona, email)
            cursor.execute (cls._InSERTAR, valores)
            log.debug(f'persona actualizadas: {persona}')
        return cursor.rowcount
    
@classmethod
def actualizar (cls, persona):
    with Conexion.obtenerConexion():
        with Conexion.obtenerCursor() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute (cls._ACTUALIZAR, valores)
            log.debug (f' Persona actualizada: {persona}')
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Los objetos eliminados son: {persona}')
                return cursor.rowcount
            

if _name__ =='__main__': 
        #Eliminar un registro
        #persona1 = Persona (id_persona=8)
        #personas_eliminados = PersonaDAO.eliminar(persona1)
        #log.debug (f'Personas eliminadas: {personas_eliminadas}')
                
        #Actualizar un registro
        #persona1 = Persona (1, 'Juan José', 'Pena', 'jjpena@mail.com')
        #personas_actualizadas = PersonaDAO.actualizar(persona1)
        #log.debut (f'Persona actualizada: {persona_actualizada}')

        # Insertar un registro
        #persona1 = Persona (nombre= 'Omero', apellido= 'Ramos', email= 'omeror@gmail.com')
        #personas_insertadas = PersonaDAO.insertar (persona1)
        #log.debug (f'Persona insertada: {personas_insertadas}')

        #Seleccionar objetos
        personas = PersonaDAO. seleccionar()
        for persona in persona: 
            log.debug(f'persona insertada: {persona_insertadas}')