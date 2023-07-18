public class Clone940AllCodeParts { 
public String getString () {
String result="";
while(true)
String message=inputGenerator.getMessage();
result+=message;
if(!message.startsWith("hi"))
return result;
}
 
 public String getString () { 
     StringBuilder msg = new StringBuilder (); 
     String read; 
     do { 
         read = inputGenerator.getMessage (); 
         msg.append (read); 
     } while (read.toLowerCase ().startsWith ("hi")); 
     return msg.toString (); 
 }

}