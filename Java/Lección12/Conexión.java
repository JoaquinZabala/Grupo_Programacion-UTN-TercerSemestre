package UTN.conexión;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexión {
    public static Connection getConnection(){
    Connection conexión= null;
    //Variable para conectarnos a la base de datos
        var baseDatos = "estudiantes2022";
        var usl = "jdbc:mysql://localhost:3306/"+baseDatos;
        var usario = "root";
        var password = "admin";

        //cargamos la clase del drive de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexión = DriverManager.getConnection(url, usuario, password);
        }catch (ClassNotFoundException | SQLException e){
            System.out.println("ocurrió un error en la conexión: "+e.getMessage());
        }//Fin catch
        return conexión;
    }//Fin método Connection
}
