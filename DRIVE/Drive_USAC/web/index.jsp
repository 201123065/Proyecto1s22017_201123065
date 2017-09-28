<%-- 
    Document   : index
    Created on : 24-sep-2017, 22:35:19
    Author     : marcosmayen
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>inicio</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">

   </head>
  <body>
      <div class="col-lg-4"></div>
      <div class="col-lg-4">
      <h1>Usac Drive </h1></div>
      <div class="col-lg-4"></div>
      <div class="col-lg-12"></div>
    <div class="col-lg-4"></div>
        <div class="col-lg-4"><p>${param.message}</p>
        <form action="login" method="post">
            <p><h2>Usuario</h2><input type="text" name ="nombre" id="user" class="form-control"/></p>
        <p><h2>password</h2><input type="text" name ="passwd" id="passwd" class="form-control"/></p>
    <p><input type="submit" name="entrar" value="Entrar" class="btn-primary col-lg-12"/></p>
        </form>
            
            <p>
                <a href="crear_usu.jsp"> o crear usuario</a>
            <a href="ver_abb" class="pull-right">ver arbol</a></p>
        </div>
    <div class="col-lg-4"></div>
    

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>
