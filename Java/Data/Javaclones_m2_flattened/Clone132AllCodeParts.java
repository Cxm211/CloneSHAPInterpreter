public class Clone132AllCodeParts { 
public static void main (String [] args) { 
     System.out.println ("Enter name"); 
     Scanner kb = new Scanner (System.in); 
     String text = kb.next (); 
     if (null == text || text.isEmpty ()) { 
         System.out.println ("Text empty"); 
     } else if (text.charAt (0) == (text.toUpperCase ().charAt (0))) { 
         System.out.println ("First letter in word " + text + " is upper case"); 
     } 
 } 
 
public static void main (String [] args) {
String str1="";
String str2=null;
String str3="Starts with upper case";
String str4="starts with lower case";
System.out.println(startWithUpperCase(str1));
System.out.println(startWithUpperCase(str2));
System.out.println(startWithUpperCase(str3));
System.out.println(startWithUpperCase(str4));
}

}