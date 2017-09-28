/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servlets;

/**
 *
 * @author marcosmayen
 */
public class header_footer {
    
    public String header(){
        String header="<!DOCTYPE html>\n" +
"<html lang=\"en\">\n" +
"  <head>\n" +
"    <meta charset=\"utf-8\">\n" +
"    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n" +
"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n" +
"    <title>inicio</title>\n" +
"\n" +
"    <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n" +
"\n" +
"   </head>\n" +
"  <body>\n" +
"";   
        return header;
    }
    
    public String footer(){
        String footer ="    <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n" +
"     <script src=\"js/bootstrap.min.js\"></script>\n" +
"  </body>";
        
        return footer;
    }
    
    
}
