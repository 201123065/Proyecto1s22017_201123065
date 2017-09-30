/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import servlets.header_footer;
import vista.sesion;
/**
 *
 * @author marcosmayen
 */
public class crear extends HttpServlet {

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
        header_footer webs = new header_footer();
        try (PrintWriter out = response.getWriter()) {
            
            HttpSession ses = request.getSession();
            
            sesion s = new sesion();
            String ccn = ses.getAttribute("nombre").toString();
            if(ccn=="null"){
                response.sendRedirect("inicio");
                
            }
            HttpSession sesion = request.getSession();
            conexion c = new conexion();
            String cad = c.verCarperas(sesion.getAttribute("nombre").toString());
            out.print(s.cabeza(ccn));
            String cad2 = "<form action=\"/action_page.php\">\n" +
"  First name: <input type=\"text\" name=\"fname\"><br>\n" +
"  Last name: <input type=\"text\" name=\"lname\"><br>\n" +
"  <input type=\"submit\" value=\"Submit\">\n" +
"</form>" ;
            out.print(cad2);
            out.print(s.pie());
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
