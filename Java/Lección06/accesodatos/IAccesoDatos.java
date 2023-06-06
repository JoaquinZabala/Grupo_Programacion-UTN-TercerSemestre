/*
Un interface no hereda de una clase objets
 */
package accesodatos;


public interface IAccesoDatos {
    int MAX_REGISTRO =10;//debemos asignar valor al declarar interface obligatoriamente
    
    //METODO INSETAR ES ABSTRACTO Y SIN CUERPO
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
    
}
