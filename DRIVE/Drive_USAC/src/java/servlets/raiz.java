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
import vista.sesion;

/**
 *
 * @author marcosmayen
 */
public class raiz extends HttpServlet {

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
            
            HttpSession ses = request.getSession();
            
            sesion s = new sesion();
            String ccn = ses.getAttribute("nombre").toString();
            if(ccn=="null"){
                response.sendRedirect("/Drive_USAC?message=" + URLEncoder.encode("sesion cerrada", "UTF-8"));
                
            }
            HttpSession sesion = request.getSession();
            conexion c = new conexion();
            String cad = c.verCarperas(sesion.getAttribute("nombre").toString());
            out.print(s.cabeza(ccn));
            out.print(ses.getAttribute("url"));
            out.print("<div class ='col-lg-4'>");
            out.print(" <form action='create_folder'  method=\"post\">");
            
            out.print("<input type='text'/  id='folder' name='folder' class ='form-control'>");
            out.print("<input type=\"submit\" name=\"entrar\" value=\"crear carpeta\" class=\"btn-primary col-lg-12 col-md-12 col-sm-12\"/>");
            
            out.print("</form>");
            out.print("</div>");
            
            
            out.print("<div class ='col-lg-4'>");
            
            out.print(" <form action=\"load_file\" method=\"post\">");
            out.print("<input type='file'/ class ='fileupload'>");
            out.print("<input type=\"submit\" name=\"entrar\" value=\"cargar archivo\" class=\"btn-success col-lg-12 col-md-12 col-sm-12\"/>");
            
            out.print("</form>");
            out.print("</div>");
            
             out.print("<div class ='col-lg-4'>");
            out.print("</div>");
             out.print("<div class ='col-lg-4'>");
            out.print("</div>");
            
            
             out.print("<div class ='col-lg-12'>");
            out.print("<br/");
            out.print("</div>");
            
             out.print("<div class ='col-lg-12'>");
            
            if (cad.equals("F")){
                out.print("la carpeta parece estar vacia");
            }else{
                out.print(cad);
                
            }
            out.print("</div>");
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
