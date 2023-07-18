public class Clone537AllCodeParts { 
public static String validName (Scanner input, Scanner histogram) { 
     HashSet < String > validInputs = new HashSet < > (); 
     while (histogram.hasNext ()) validInputs.add (histogram.next ()); 
     while (true) { 
         String userInput = input.next (); 
         if (validInputs.contains (userInput)) return userInput; 
         System.out.println ("invalid input"); 
     } 
 } 
 
public static String validName (Scanner input, Scanner histogram) {
String user="";
String name=input.next();
if(histogram.findInLine(name) != null)
System.out.println("This name exist");
System.out.println("Name not found");
user=validName(input,histogram);
return user;
}

}