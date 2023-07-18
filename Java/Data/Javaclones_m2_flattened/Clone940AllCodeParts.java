public class Clone940AllCodePartsm2 {  
 public String getString () { 
     String result = ""; 
     while (true) { 
         String message = inputGenerator.getMessage (); 
         result += message; 
         if (! message.startsWith ("hi")) { 
             break; 
         } 
     } 
     return result; 
 }

public String getString () {
StringBuilder msg=new StringBuilder();
String read;
read=inputGenerator.getMessage();
msg.append(read);
return msg.toString();
}

}