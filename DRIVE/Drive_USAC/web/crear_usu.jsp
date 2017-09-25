<%-- 
    Document   : crear_usu
    Created on : 24-sep-2017, 23:04:24
    Author     : marcosmayen
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Crear usuario</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">

   </head>
  <body>
      <div clas="col-lg-4">.</div>
      <div clas="col-lg-4">
        <h1>Crear usuario</h1>
      </div>
      <div clas="col-lg-4">.</div>
      <div class="col-lg-12"></div>
      <div class="col-lg-4"></div>
      
      <div class="col-lg-4">
        <form action="crear" nethod="post">
            <p>Nombre<input type="text" name ="nombre" id="user" class="pull-right col-lg-8"/></p>
            <p>Contrase&ntilde;<input type="text" name ="passwd" id="passwd" class="pull-right col-lg-8"/></p>
            <p>Confirmar contrase&ntilde;a<input type="text" name ="p2" id="p2" class="pull-right col-lg-8"/></p>
            <p><input type="submit" name="crear" value="crear" class="btn-primary col-lg-12"/></p>
        </form>
        </div>
      <div class="col-lg-4"></div>
      
    </body>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>