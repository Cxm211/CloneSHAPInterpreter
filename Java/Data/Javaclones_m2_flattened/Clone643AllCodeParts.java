public class Clone643AllCodePartsm2 {  
 public static String join (Collection s, String delimiter) { 
     StringBuffer buffer = new StringBuffer (); 
     Iterator iter = s.iterator (); 
     while (iter.hasNext ()) { 
         buffer.append (iter.next ()); 
         if (iter.hasNext ()) { 
             buffer.append (delimiter); 
         } 
     } 
     return buffer.toString (); 
 }

public static String join (Object [] objects, String delimiter) {
if(objects.length == 0)
return "";
int capacityGuess=(objects.length * objects[0].toString().length()) + ((objects.length - 1) * delimiter.length());
StringBuilder ret=new StringBuilder(capacityGuess);
ret.append(objects[0]);
for([int i=1] i < objects.length [i++])
ret.append(delimiter);
ret.append(objects[i]);
return ret.toString();
}

}