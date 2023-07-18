public class Clone13AllCodeParts { 
public int countLines (String filename) throws IOException { 
     LineNumberReader reader = new LineNumberReader (new FileReader (filename)); 
     int cnt = 0; 
     String lineRead = ""; 
     while ((lineRead = reader.readLine ()) != null) { 
     } 
     cnt = reader.getLineNumber (); 
     reader.close (); 
     return cnt; 
 } 
 
public static int countLines (File input) throws IOException {
int count=1;
for([int aChar=0] aChar != -1 [aChar=is.read()])
count+=aChar == '\n' ? 1 : 0;
return count;
}

}