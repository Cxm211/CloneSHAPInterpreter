public class Clone345AllCodePartsm2 {  
 public static void main (String [] args) { 
     String name = "AnuvratAnuvra"; 
     char [] arr = name.toCharArray (); 
     HashMap < Character, Integer > map = new HashMap < Character, Integer > (); 
     for (char val : arr) { 
         map.put (val, map.containsKey (val) ? map.get (val) + 1 : 1); 
     } 
     for (Entry < Character, Integer > entry : map.entrySet ()) { 
         if (entry.getValue () > 1) { 
             Character key = entry.getKey (); 
             Object value = entry.getValue (); 
             System.out.println (key + ":" + value); 
         } 
     } 
 }

public static void main (String [] args) {
String test="The quick brown fox jumped over the lazy dog.";
int countA=0, countO=0, countSpace=0, countDot=0;
for([int i=0] i < test.length() [i++])
countA++;
countO++;
countSpace++;
countDot++;
System.out.printf("%s%d%n%s%d%n%s%d%n%s%d","A: ",countA,"O: ",countO,"Space: ",countSpace,"Dot: ",countDot);
}

}