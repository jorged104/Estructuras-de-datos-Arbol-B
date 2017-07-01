
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.MalformedURLException;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Jorge
 */
public class insertar {
    public String jugador;
    public String columna;
    public String fila;
    public String tipo;
    public String modo;
    public String direccion;

    public insertar(String jugador, String columna, String fila, String tipo, String modo, String direccion) {
        this.jugador = jugador;
        this.columna = columna;
        this.fila = fila;
        this.tipo = tipo;
        this.modo = modo;
        this.direccion = direccion;
    }
    public void ejecutar() throws MalformedURLException, UnsupportedEncodingException, IOException
    {
        String[] data = {this.jugador,this.columna,this.fila,this.tipo,this.modo,this.direccion};
                          String x = String.valueOf(letra(data[1]));
                          
                         
                          switch(data[3])
                          {
                              case "1":  // Satelites =) 
                                  PeticionPost peticionSatelite = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                  peticionSatelite.add("x", x);
                                  peticionSatelite.add("z", "2");
                                  peticionSatelite.add("y", data[2]);
                                  peticionSatelite.add("dato","Satelite");
                                  peticionSatelite.add("usuario",data[0]);
                                  peticionSatelite.getRespueta();
                                  break;
                              case "2":  // Aviones Listo =) 
                                  int Ax = letra(data[1]);
                                  
                                  if (data[4].equals("1"))
                                  {
                                    for( int i1 = (Ax-1) ; i1 < Ax+2 ; i1++)
                                    {
                                    PeticionPost peticionAvion1 = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                    peticionAvion1.add("x", String.valueOf(i1));
                                    peticionAvion1.add("z", "1");
                                    peticionAvion1.add("y", data[2]);
                                    peticionAvion1.add("dato","Avion");
                                    peticionAvion1.add("usuario",data[0]);
                                    peticionAvion1.getRespueta();
                                    }
                                    
                                    for (int i2 = Integer.parseInt(data[2])+1 ; i2 < Integer.parseInt(data[2])+4 ;i2++)
                                    {
                                        PeticionPost peticionAvion1 = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                        peticionAvion1.add("x", String.valueOf(Ax));
                                        peticionAvion1.add("z", "1");
                                        peticionAvion1.add("y", String.valueOf(i2));
                                        peticionAvion1.add("dato","Avion");
                                        peticionAvion1.add("usuario",data[0]);
                                        peticionAvion1.getRespueta();
                                    } 
                                }
                                  if(data[4].equals("2")) 
                                  {
                                    for( int i1 = (Ax-1) ; i1 < Ax+2 ; i1++)
                                    {
                                    PeticionPost peticionAvion1 = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                    peticionAvion1.add("x", String.valueOf(i1));
                                    peticionAvion1.add("z", "1");
                                    peticionAvion1.add("y", data[2]);
                                    peticionAvion1.add("dato","Avion");
                                    peticionAvion1.add("usuario",data[0]);
                                    peticionAvion1.getRespueta();
                                    } 
                                    int y = Integer.parseInt(data[2])+1;
                                    PeticionPost peticionAvion1 = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                    peticionAvion1.add("x", String.valueOf(Ax));
                                    peticionAvion1.add("z", "1");
                                    peticionAvion1.add("y", String.valueOf(y));
                                    peticionAvion1.add("dato","Avion");
                                    peticionAvion1.add("usuario",data[0]);
                                    peticionAvion1.getRespueta();
                                  }
                                 break;
                              case "3":
                                  int largo = Integer.parseInt(data[4]);
                                  int Ax2 = letra(data[1]);
                                  int y2  = Integer.parseInt(data[2]);
                                  if(data[5].equals("1")) //1 horizontal 2 vertical 
                                  {
                                      
                                    for( int i1 = (Ax2) ; i1 < Ax2+largo ; i1++)
                                    {
                                    PeticionPost peticionBarco = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                    peticionBarco.add("x", String.valueOf(i1));
                                    peticionBarco.add("z", "0");
                                    peticionBarco.add("y", data[2]);
                                    peticionBarco.add("dato","Barco");
                                    peticionBarco.add("usuario",data[0]);
                                    peticionBarco.getRespueta();
                                    } 
                                  }
                                  else
                                  {
                                    for( int i1 = (y2) ; i1 < y2+largo ; i1++)
                                    {
                                    PeticionPost peticionBarco = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                    peticionBarco.add("x", String.valueOf(Ax2));
                                    peticionBarco.add("z", "0");
                                    peticionBarco.add("y", String.valueOf(i1));
                                    peticionBarco.add("dato","Barco");
                                    peticionBarco.add("usuario",data[0]);
                                    peticionBarco.getRespueta();
                                    }  
                                  }
                              break;
                              case "4":
                                    int largos = Integer.parseInt(data[4]);
                                  int Ax2s = letra(data[1]);
                                         int y2s  = Integer.parseInt(data[2]);

                                  if(data[5].equals("1")) //1 horizontal 2 vertical 
                                  {
                                      
                                    for( int i1 = (Ax2s) ; i1 < Ax2s+largos ; i1++)
                                    {
                                    PeticionPost peticionBarco = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                    peticionBarco.add("x", String.valueOf(i1));
                                    peticionBarco.add("z", "-1");
                                    peticionBarco.add("y", data[2]);
                                    peticionBarco.add("dato","Submarino");
                                    peticionBarco.add("usuario",data[0]);
                                    peticionBarco.getRespueta();
                                    } 
                                  }
                                  else
                                  {
                                    for( int i1 = (y2s) ; i1 < y2s+largos ; i1++)
                                    {
                                    PeticionPost peticionBarco = new PeticionPost("http://localhost:5000/InsertarEnMatriz");
                                    peticionBarco.add("x", String.valueOf(Ax2s));
                                    peticionBarco.add("z", "-1");
                                    peticionBarco.add("y", String.valueOf(i1));
                                    peticionBarco.add("dato","Submarino");
                                    peticionBarco.add("usuario",data[0]);
                                    peticionBarco.getRespueta();
                                    }  
                                  }
                                break;
                          }
    }
    public int letra(String letra)
    {
     String[] letras = {" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};   
        for (int i = 0 ; i < letras.length ; i++)
        {
            if (letras[i].equals(letra))
            {
                return i;
            }
        }
        return 255;
    }
}
