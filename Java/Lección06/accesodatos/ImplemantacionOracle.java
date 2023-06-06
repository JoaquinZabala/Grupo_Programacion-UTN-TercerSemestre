/*
Implementamos en otra base de datos
 */
package accesodatos;


public class ImplemantacionOracle implements IAccesoDatos{
//Si eliminamos un metodo, marca error asique debemos marcar la clase como abstracta
    
    @Override
    public void insertar() {
        System.out.println("Insertar desde Oracle");
    }

    @Override
    public void listar() {
         System.out.println("Listar desde Oracle");
   }

    @Override
    public void actualizar() {
         System.out.println("Actualizar desde Oracle");
    }

    @Override
    public void eliminar() {
         System.out.println("Eliminar desde Oracle");
  }
    
}
