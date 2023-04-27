
package enumeraciones;


public enum Continentes {
    AFRICA(53, "1.2 billones"),
    EUROPA(45, "1.3 billones"),
    ASIA(56, "2.2 billones"),
    AMERICA(24, "23.9 billones"),
    OCEANIA(12, "2.1 billones");
    
    private final int paises;
    private String habitantes;
    
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }
    //Método get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
    
}
