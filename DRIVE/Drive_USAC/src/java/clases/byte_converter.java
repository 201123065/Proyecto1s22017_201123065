/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package clases;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.*;
import java.nio.file.Files;

/**
 *
 * @author marcosmayen
 */
public class byte_converter {
    
    public static byte[] getbytes(File f) throws FileNotFoundException, IOException{
        byte[] buffer = new byte[1024];
        ByteArrayOutputStream os = new ByteArrayOutputStream();
        FileInputStream fis = new FileInputStream(f);
        int read;
        while((read=fis.read(buffer))!=-1){
            os.write(buffer,0,read);
        }
        fis.close();
        os.close();
        return os.toByteArray();
        
    }
    
    public  static void toFile(byte[] data,File destino){
        try{
            FileOutputStream FOS = new FileOutputStream(destino);
            FOS.write(data);
            FOS.close();
            
            
            
        }catch (Exception e){
            
        }
        
    }
    
    
    
}
