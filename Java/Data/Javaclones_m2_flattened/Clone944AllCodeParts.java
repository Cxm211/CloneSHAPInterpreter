public class Clone944AllCodeParts { 
public static void main (String [] args) throws Exception { 
     Console console = System.console (); 
     if (console == null) { 
         System.out.println ("Unable to fetch console"); 
         return; 
     } 
     String line = console.readLine (); 
     console.printf ("I saw this line: %s", line); 
 } 
 
public static void main (String [] args) throws IOException {
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
System.out.print("Enter String");
String s=br.readLine();
System.out.print("Enter Integer:");
int i=Integer.parseInt(br.readLine());
System.err.println("Invalid Format!");
}

}