/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vista;

/**
 *
 * @author marcosmayen
 */
public class sesion {
    
    public String cabeza(String nombre){
        return"<html lang=\"en\">\n" +
"\n" +
"<head>\n" +
"\n" +
"    <meta charset=\"utf-8\">\n" +
"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n" +
"    <meta name=\"description\" content=\"\">\n" +
"    <meta name=\"author\" content=\"\">\n" +
"\n" +
"    <title>Simple Sidebar - Start Bootstrap Template</title>\n" +
"\n" +
"    <!-- Bootstrap core CSS -->\n" +
"    <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n" +
"\n" +
"    <!-- Custom styles for this template -->\n" +
"    <link href=\"css/simple-sidebar.css\" rel=\"stylesheet\">\n" +
"\n" +
"</head>\n" +
"\n" +
"<body>\n" +
"\n" +
"    <div id=\"wrapper\">\n" +
"\n" +
"        <!-- Sidebar -->\n" +
"        <div id=\"sidebar-wrapper\">\n" +
"            <ul class=\"sidebar-nav\">\n" +
"                <li class=\"sidebar-brand\">\n" +
"                    <a href=\"#\">\n" +nombre+
"                    </a>\n" +
"                </li>\n" +
"                <li>\n" +
"                    <a href=\"raiz\">/</a>\n" +
"                </li>\n" +
"                <li>\n" +
"                    <a href=\"#\">crear carpeta</a>\n" +
"                </li>\n" +
"                <li>\n" +
"                    <a href=\"#\">cargar archivo</a>\n" +
"                </li>\n" +
"                <li>\n" +
"                    <a href=\"#\">compartir archivo</a>\n" +
"                </li>\n" +
"                <li>\n" +
"                    <a href=\"#\">ver arbol</a>\n" +
"                </li>\n" +
"            </ul>\n" +
"        </div>\n" +
"        <!-- /#sidebar-wrapper -->\n" +
"\n" +
"        <!-- Page Content -->\n" +
"        <div id=\"page-content-wrapper\">\n" +
"            <div class=\"container-fluid\">\n" +
"                <h1>Bienvenido "+nombre+"</h1>\n" +
"                <a href=\"#menu-toggle\" class=\"btn btn-secondary\" id=\"menu-toggle\">Menu</a>\n" +
"            </div>";
    }
    
    
    public String pie(){
        return " </div>\n" +
"        <!-- /#page-content-wrapper -->\n" +
"\n" +
"    </div>\n" +
"    <!-- /#wrapper -->\n" +
"\n" +
"    <!-- Bootstrap core JavaScript -->\n" +
"    <script src=\"jquery/jquery.min.js\"></script>\n" +
"    <script src=\"popper/popper.min.js\"></script>\n" +
"    <script src=\"bootstrap/js/bootstrap.min.js\"></script>\n" +
"\n" +
"    <!-- Menu Toggle Script -->\n" +
"    <script>\n" +
"    $(\"#menu-toggle\").click(function(e) {\n" +
"        e.preventDefault();\n" +
"        $(\"#wrapper\").toggleClass(\"toggled\");\n" +
"    });\n" +
"    </script>\n" +
"\n" +
"</body>\n" +
"\n" +
"</html>\n" +
"\n";
    }
    
}
