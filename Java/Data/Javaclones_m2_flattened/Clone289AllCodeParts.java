public class Clone289AllCodePartsm2 {  
 public static String [] tokenizer (String text, String [] delims) { 
     for (String delim : delims) { 
         int i = text.indexOf (delim); 
         if (i >= 0) { 
             String [] tail = tokenizer (text.substring (i + delim.length ()), delims); 
             String [] list = new String [tail.length + 2]; 
             list [0] = text.substring (0, i); 
             list [1] = delim; 
             System.arraycopy (tail, 0, list, 2, tail.length); 
             return list; 
         } 
     } 
     return new String [] {text}; 
 }

public Object [] tokenizer (String value, String [] delimeters) {
List<String> list=new ArrayList<String>();
if(value.contains(s))
String[] strArr=value.split("\\" + s);
list.add(str);
if(!list.contains(s))
list.add(s);
Object[] newValues=list.toArray();
return newValues;
}

}