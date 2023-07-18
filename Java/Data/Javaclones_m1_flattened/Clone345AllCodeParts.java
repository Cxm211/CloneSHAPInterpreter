public class Clone345AllCodeParts { 
public static void main (String [] args) {
String name="AnuvratAnuvra";
char[] arr=name.toCharArray();
HashMap<Character,Integer> map=new HashMap<Character,Integer>();
map.put(val,map.containsKey(val) ? map.get(val) + 1 : 1);
if(entry.getValue() > 1)
Character key=entry.getKey();
Object value=entry.getValue();
System.out.println(key + ":" + value);
}
 
 public static void main (String [] args) { 
     String test = "The quick brown fox jumped over the lazy dog."; 
     int countA = 0, countO = 0, countSpace = 0, countDot = 0; 
     for (int i = 0; 
     i < test.length (); i ++) { 
         switch (test.charAt (i)) { 
             case 'a' : 
             case 'A' : 
                 countA ++; 
                 break; 
             case 'o' : 
             case 'O' : 
                 countO ++; 
                 break; 
             case ' ' : 
                 countSpace ++; 
                 break; 
             case '.' : 
                 countDot ++; 
                 break; 
         } 
     } 
     System.out.printf ("%s%d%n%s%d%n%s%d%n%s%d", "A: ", countA, "O: ", countO, "Space: ", countSpace, "Dot: ", countDot); 
 }

}