/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import javax.servlet.MultipartConfigElement;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

/**
 *
 * @author Jorge
 */
@WebServlet(urlPatterns = {"/subir"})
@MultipartConfig(
        fileSizeThreshold   = 1024 * 1024 * 1,  // 1 MB
        maxFileSize         = 1024 * 1024 * 10, // 10 MB
        maxRequestSize      = 1024 * 1024 * 15, // 15 MB
        location            = "/Uploads"
)
public class subir extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
//    @MultipartConfig
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
            try (PrintWriter out = response.getWriter()) {
            // Utiliza Part para accesar al objeto que viene de parametro
            Part p1 = request.getPart("archivo_parametro");
            String tipo = request.getParameter("selecciona");
            
            InputStream is = p1.getInputStream();
            String datos = convertStreamToString(is);
            String[] resultado = datos.split("\n");
           switch (tipo)
           {
               case "Usuarios":
                      for(int i = 1 ; i < resultado.length;i++)
                      {
                          String linea = resultado[i];
                          String[] data = linea.split(",");
                          PeticionPost post = new PeticionPost("http://localhost:5000/registroAutomatico");
                          post.add("usuario", data[0]);
                          post.add("contra",data[1]);
                          post.add("on",data[2]);
                          post.getRespueta();
                      }
                   break;
               case "Juego":
                      for(int i = 1 ; i < resultado.length;i++)
                      {
                          String linea = resultado[i];
                          String[] data = linea.split(",");
                          PeticionPost post2 = new PeticionPost("http://localhost:5000/registroDeJuegos");
                          post2.add("usuarioBase", data[0]);
                          post2.add("oponente",data[1]);
                          post2.add("TirosR",data[2]);
                          post2.add("TirosA", data[3]);
                          post2.add("TirosF", data[4]);
                          post2.add("Gano",data[5]);
                          post2.add("TirosRecibidos", data[6]);
                          post2.getRespueta();
                      }                    
                   break;
               case "naves":
                   for(int i = 1 ; i < resultado.length;i++)
                      {
                          String linea = resultado[i];
                          String[] data = linea.split(",");
                          
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
                          //out.println());
                      }
                break;
               case "JuegoActual":
                   PeticionPost post2 = new PeticionPost("http://localhost:5000/setgame");
                    String linea = resultado[1];
                    String[] data = linea.split(",");
                   post2.add("usuario1", data[0]);
                   post2.add("usuario2", data[1]);
                   post2.add("x", data[2]);
                   post2.add("y", data[3]);
                   post2.add("mod", data[4]);
                   String [] tiempo = data[5].split(":");
                   post2.add("minutos", tiempo[0]);
                   post2.add("segundos", tiempo[1]);
                   post2.add("disparo", data[6]);
                   post2.add("rafagas", data[7]);
                   post2.getRespueta();
                          
                   break;
                case "contactos":
                      for(int i = 1 ; i < resultado.length;i++)
                      {
                          String contactos = resultado[i];
                          String[] datac = contactos.split(","); 
                         PeticionPost insertarA = new PeticionPost("http://localhost:5000/InsertarAmigo");
                                  insertarA.add("usuario",datac[0]);
                                  insertarA.add("amigo",datac[1]);
                                  insertarA.add("pas",datac[2]);  
                                  insertarA.getRespueta();
                      }
                  break;
                case "historial":
                    for(int i = 1 ; i < resultado.length;i++)
                      {
                          String historial = resultado[i];
                          String[] datac = historial.split(","); 
                         PeticionPost ph = new PeticionPost("http://localhost:5000/InsertarEnB");
                                  ph.add("x",datac[0]);
                                  ph.add("y",datac[1]);
                                  ph.add("tiro",datac[2]);
                                  ph.add("res",datac[3]);
                                  ph.add("tipo",datac[4]);
                                  ph.add("emisor",datac[5]);
                                  ph.add("receptor",datac[6]);
                                  ph.add("fecha",datac[7]);
                                  ph.add("tiempo",datac[8]);
                                  ph.add("NoTiro",datac[9]);
                                  ph.getRespueta();
                      }
                    break;
                    case "tiros":
                    for(int i = 1 ; i < resultado.length;i++)
                      {
                          String historial = resultado[i];
                          String[] tiro = historial.split(","); 
                         PeticionPost ph = new PeticionPost("http://localhost:5000/tiro");
                                  ph.add("usuario",tiro[0]);
                                  ph.add("x",String.valueOf(letra(tiro[1])));
                                  ph.add("y",tiro[2]);
                                  ph.add("z","2");
                                  ph.getRespueta();
                      }
                    break;
           }
            //out.print(resultado[0]);
            //out.print(tipo);
            //response.sendRedirect("/cliente/");
            out.print("Listo");
            is.close();
           
        } catch (Exception ex) {           
           ex.printStackTrace();
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

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }
    
    static String convertStreamToString(java.io.InputStream is) {
    java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A");
    return s.hasNext() ? s.next() : "";
}
    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
