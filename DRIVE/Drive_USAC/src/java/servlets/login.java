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

/**
 *
 * @author marcosmayen
 */
public class login extends HttpServlet {

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
            String usu = request.getParameter("nombre");
            String pass = request.getParameter("passwd");
            /* TODO output your page here. You may use following sample code. */
            conexion cu = new conexion();
            
             out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet logea</title>");            
            out.println("</head>");
            out.println("<body>");
            out.println(cu.Login(usu, pass));
            out.println(usu+"___"+pass);
            
            if(cu.Login(usu, pass).equals("V")){
                out.println("<h1>SIMON ENTRO</h1>");
                HttpSession session = request.getSession();
                session.setAttribute("usuario", usu);
                    out.println(cu.getSuper(session.getId()));
            out.println(cu.getSuper(session.getId()));
                //if(cu.getSuper(session.getId()).equals("V")){
                 //   response.sendRedirect("/battleship_prueba/admin.jsp");
               // }
                //else{
                  //  response.sendRedirect("/battleship_prueba/Menu.jsp");
                    
                //}
            }
            else{
                out.println("<h1>anomanoasdasdsa</h1>");
                
            
            }
            out.println("<h1>Servlet logea at " + request.getContextPath() + "</h1>");
            out.println("</body>");
            out.println("</html>");
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
