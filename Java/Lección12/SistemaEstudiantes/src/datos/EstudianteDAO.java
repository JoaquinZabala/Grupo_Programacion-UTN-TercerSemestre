package UTN.datos;

import UTN.dominio.Estudiante;

import static UTN.conexion.Conexion.getConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;


public class EstudianteDAO {
    //Método listar
    public List<Estudiante> listarEstudiantes() {

        //Creamos una lista de la clase Estudiante
        List<Estudiante> estudiantes = new ArrayList<>();

        //Creamos algunos objetos que son necesarios para comunicarnos con la bd
        PreparedStatement ps; //renombramos, envia la sentencia sql
        ResultSet rs; //renombramos, obtenemos el resultado obtenido de la bd

        //Creamos un objeto de tipo conexión
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 ORDER BY idestudiantes2022";
        try { //Enviamos la consulta hacia la base de datos
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery(); // recibimos la ejecucion del querry que estamos enviando
            while (rs.next()) { //mientras tengamos registros para iterar va a serguir operando
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2022"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //Agrega a la lista
                estudiantes.add(estudiante);

            }
        } catch (Exception e) {
            System.out.println("Ocurrió un error al seleccionar datos: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            } catch (Exception e){
                System.out.println("Ocurrio un error al cerrar la conexion: "+e.getMessage());
            }
        }//Fin finally
        return estudiantes;
    }//Fin metodo listar

    //Metodo por id -> find by id
    public boolean buscarEstudiantePorId(Estudiante estudiante){
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 WHERE idestudiantes2022=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery();
            if (rs.next()) {
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true; //se encontro un registro
            } // Fin IF
        } catch (Exception e) {
            System.out.println("Ocurrio un error al buscar estudiante: "+e.getMessage());
        } // Fin Catch
        finally{
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("ocurrio un error al cerrar conexion"+e.getMessage());
            }//fin Catch
        }//fin Finally
        return false;
    }

    //Método agregar un nuevo estudiantes
    public boolean agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES (?, ?, ?, ?)";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.execute();
            return true;
        } catch(Exception e){
            System.out.println("Ocurrio un error al agregar estudiante: " + e.getMessage());
        } //Fin Cacth
        finally {
            try{
                con.close();
            }catch (Exception e){
                System.out.println("Error al cerrar la conexión"+e.getMessage());
            }
        }// Fin Finaly
        return false;
    } // Fin Método agregar estudiante

    // Método para modificar estudiante
    public boolean modificarEstudiante(Estudiante estudiante) {
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "UPDATE estudiante2022 SET nombre=?, apellido=?, telefono=?, email=? WHERE idestudiantes2022=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1,estudiante.getNombre());
            ps.setString(2,estudiante.getApellido());
            ps.setString(3,estudiante.getTelefono());
            ps.setString(4,estudiante.getEmail());
            ps.setInt(5,estudiante.getIdEstudiante());
            ps.execute();
            return true;
        }catch (Exception e){
            System.out.println("Error al modificar estudiante: "+e.getMessage());
        }// Fin Catch
        finally {
            try{
                con.close();
            }catch (Exception e){
                System.out.println("Error al cerrar conexión: "+e.getMessage());
            }// Fin Catch
        }// Fin Finaly
        return false;
    }// Fin Método modificar


    public static void main(String[] args) {
        var estudiantesDao = new EstudianteDAO();
        // Modificar estudiante
        var estudianteModificado = new Estudiante(1, "Juan Carlos", "Juarez", "123456","juen@email.com");
        var modificado = estudiantesDao.modificarEstudiante(estudianteModificado);
        if(modificado)
            System.out.println("Estudiante modificado: "+estudianteModificado);
        else
            System.out.println("No se modifico el estudiante: "+estudianteModificado);

        //Agregar estudiante
                var nuevoestudiante = new Estudiante("Carlos","Lara","123456","carlosl@email.com");
                var agregado = estudiantesDao.agregarEstudiante(nuevoestudiante);
                if(agregado)
                    System.out.println("Estudiante agregado:"+nuevoestudiante);
                else
                    System.out.println("No se a agregado estudiante: "+nuevoestudiante);
        //Listar los estudiantes
        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudiantesDao.listarEstudiantes();
        estudiantes.forEach(System.out::println); //Funcion lambda para imprimir



        //Buscar por id
//        var estudiante1 = new Estudiante(1);
//        System.out.println("Estudiantes antes de la busqueda"+estudiante1);
//        var encontrado = estudiantesDao.buscarEstudiantePorId(estudiante1);
//        if(encontrado){
//            System.out.println("Estudiante encontrado"+ estudiante1);
//        }else{
//            System.out.println("No se encontro el estudiante: "+ estudiante1.getIdEstudiante());
        }
    }







