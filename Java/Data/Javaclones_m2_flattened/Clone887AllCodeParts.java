public class Clone887AllCodePartsm2 {  
 public static void main (String args []) { 
     String s1 = "a b c"; 
     int s1_length = s1.length (); 
     System.out.println (s1_length); 
     String s2 = s1.replace (" ", ""); 
     int s2_length = s2.length (); 
     System.out.println (s2_length); 
     System.out.println ("No of spaces = " + (s1_length - s2_length)); 
 }

public static void main (String [] args) {
String word="a b c";
int i=0, spaceCount=0;
while(i < word.length())
if(word.charAt(i) == ' ')
spaceCount++;
i++;
System.out.println("Spaces in string: " + spaceCount);
}

}