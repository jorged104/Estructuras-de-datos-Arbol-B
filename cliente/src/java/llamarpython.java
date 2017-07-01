/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Jorge
 */
@WebServlet(urlPatterns = {"/llamarpython"})
public class llamarpython extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            /*out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet llamarpython</title>");            
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Servlet llamarpython at " + request.getContextPath() + "</h1>");
            out.println("</body>");
            out.println("</html>");*/
            PeticionPost post;
            String res;
            String tipo = request.getParameter("tipo");
            switch (tipo)
            {
                case "login":
                    post= new PeticionPost("http://localhost:5000/login");
                    post.add("usuario",request.getParameter("usuario"));
                    post.add("contra",request.getParameter("password"));
                     res = post.getRespueta();
                    out.println(res);
                break;
                case "tablas":
                    post= new PeticionPost("http://localhost:5000/getTabla");
                    post.add("z",request.getParameter("z"));
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                    break;
                case "enjuego":
                    post= new PeticionPost("http://localhost:5000/enjuego");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                break;
                 case "enturno":
                    post= new PeticionPost("http://localhost:5000/enturno");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                break;
                case "getGame":
                    post= new PeticionPost("http://localhost:5000/getGame");
                    res = post.getRespueta();
                    out.println(res);
                break;
                case "getcubo":
                    post= new PeticionPost("http://localhost:5000/cuboNaves");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                 break;
                 case "getcuboinicial":
                    post= new PeticionPost("http://localhost:5000/cuboNavesInicial");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                 break; 
                 case "geta":
                    post= new PeticionPost("http://localhost:5000/cuboTirosA");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                 break; 
                 case "getf":
                    post= new PeticionPost("http://localhost:5000/cuboTirosF");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                 break; 
                 case "getusuarios":
                    post= new PeticionPost("http://localhost:5000/getusuarios");
                
                    res = post.getRespueta();
                    out.println(res);
                 break;
                 case "getespejo":
                    post= new PeticionPost("http://localhost:5000/getespejo");
                    res = post.getRespueta();
                    out.println(res);
                 break;
                case "estadisticas":
                    post= new PeticionPost("http://localhost:5000/getEstadisticas");
                    res = post.getRespueta();
                    out.println(res);
                 break;
                 case "disparo":
                    post= new PeticionPost("http://localhost:5000/tiro");
                    post.add("usuario",request.getParameter("usuario"));
                    post.add("x",request.getParameter("x"));
                    post.add("y",request.getParameter("y"));
                    post.add("z",request.getParameter("z"));
                    res = post.getRespueta();
                    out.println(res);
                 break;
                 case "insert":
                     insertar a = new insertar(request.getParameter("usuario"), request.getParameter("col"), request.getParameter("fila"), request.getParameter("nave"), request.getParameter("modo"), request.getParameter("dire"));
                     a.ejecutar();
                     out.print("yes");
                     break;
                 case "gane":
                    post= new PeticionPost("http://localhost:5000/gane");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                 break;  
                  case "listausuarios":
                    post= new PeticionPost("http://localhost:5000/listausuarios");
                    res = post.getRespueta();
                    out.println(res);
                 break; 
                  case "eliminarus":
                       post= new PeticionPost("http://localhost:5000/eliminarus");
                    post.add("usuario",request.getParameter("usuario"));
                    res = post.getRespueta();
                    out.println(res);
                      break;
                    case "editarus":
                    post= new PeticionPost("http://localhost:5000/editarus");
                    post.add("usuario",request.getParameter("usuario"));
                    post.add("contra",request.getParameter("contra"));
                    res = post.getRespueta();
                    out.println(res);
                      break;
                    
            }
        }
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
