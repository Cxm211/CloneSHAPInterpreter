public class Clone289AllCodeParts { 
public static String [] tokenizer (String text, String [] delims) {
int i=text.indexOf(delim);
if(i >= 0)
String[] tail=tokenizer(text.substring(i + delim.length()),delims);
String[] list=new String[tail.length + 2];
list[0]=text.substring(0,i);
list[1]=delim;
System.arraycopy(tail,0,list,2,tail.length);
return list;
return new String[]{text};
}
 
 public Object [] tokenizer (String value, String [] delimeters) { 
     List < String > list = new ArrayList < String > (); 
     for (String s : delimeters) { 
         if (value.contains (s)) { 
             String [] strArr = value.split ("\\" + s); 
             for (String str : strArr) { 
                 list.add (str); 
                 if (! list.contains (s)) { 
                     list.add (s); 
                 } 
             } 
         } 
     } 
     Object [] newValues = list.toArray (); 
     return newValues; 
 }

}