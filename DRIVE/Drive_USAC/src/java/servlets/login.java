/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import servlets.header_footer;
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
            header_footer web = new header_footer();
            out.print(web.header());
            String usu = request.getParameter("nombre");
            String pass = request.getParameter("passwd");
            out.print(usu);
            out.print("<br/>");
            out.print(pass);
            out.print("<br/>");
            request.getSession().invalidate();
            conexion cu = new conexion();
            HttpSession sesion = request.getSession();
            if (usu!=null && pass!=null){
                if(cu.Login(usu, pass).equals("F")){
                    String message="El usuario o la contrase&ntilde;a estan equivocados, favor volver a intentar";
                    response.sendRedirect("index.jsp?message=" + URLEncoder.encode(message, "UTF-8"));

                }else{
                    sesion.setAttribute("url", usu+"/");
                    if (sesion.getAttribute("nombre")==null){
                        sesion.setAttribute("nombre", usu);
                        out.print("bienvenido :) "+sesion.getAttribute("nombre"));
                        response.sendRedirect("raiz");

                    }else{
                        out.print("bienvenido "+sesion.getAttribute("nombre"));
                        response.sendRedirect("raiz");
                    }

                }
            }else{
                    String message="";
                    response.sendRedirect("inicio");
            }
            
            
            out.print(web.footer());
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
